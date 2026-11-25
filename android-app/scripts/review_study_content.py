"""Validate private content/review files and render an offline reviewer workspace."""
import argparse
from collections import Counter
from datetime import date
from hashlib import sha256
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

from acquire_study_content import PART_ENDS, write_json
from activate_study_content import (
    SHA, activate_groups, evidence_matches, group_assets, item_binding, nonempty, optional_rows, source_keys,
    valid_source, verify_media,
)
from extend_study_content import ROOT02, save_json, seed_previous, snapshot_source
from listening_manifest import read_blob, read_json

STATUSES = {"SOURCE_ONLY", "APPROVED", "REVOKED"}
GROUP_SIZES = {1: (1,), 2: (1,), 3: (3,), 4: (3,), 5: (1,), 6: (4,), 7: (2, 3, 4, 5)}
ID = re.compile(r"[a-zA-Z0-9_.:-]{1,100}")


def source_host(url):
    if not isinstance(url, str) or len(url) > 600 or any(ord(c) <= 32 or c == "\\" for c in url):
        raise ValueError("Invalid source URL")
    parsed = urlsplit(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username is not None or parsed.port not in (None, 443):
        raise ValueError("Source must identify an HTTPS publisher")
    return parsed.hostname


def validate_owner_group(row, root, used_versions):
    fields = {"id", "part", "source", "version", "items", "audio", "image", "extraImages", "passage",
              "audioItems", "imageItems", "passageItems"}
    if (not isinstance(row, dict) or row.keys() - fields
            or not isinstance(row.get("id"), str) or not ID.fullmatch(row["id"])):
        raise ValueError("Invalid owner group fields or ID")
    part, items, version = row.get("part"), row.get("items"), row.get("version")
    source_host(row.get("source"))
    if type(part) is not int or part not in GROUP_SIZES or not isinstance(items, list) or len(items) not in GROUP_SIZES[part]:
        raise ValueError("Invalid owner Part or group size")
    if not isinstance(version, str) or not SHA.fullmatch(version):
        raise ValueError("Invalid owner source revision")
    if version not in used_versions:
        path = root / "sources" / f"{version}.bin"
        if path.resolve().parent != (root / "sources").resolve() or sha256(read_blob(path)).hexdigest() != version:
            raise ValueError("Owner source snapshot hash mismatch")
        used_versions.add(version)
    for item in items:
        if not isinstance(item, dict) or set(item) != {"id", "number", "prompt", "choices"}:
            raise ValueError("Unexpected owner question fields")
        choices = item["choices"]
        if (not isinstance(item["id"], str) or not ID.fullmatch(item["id"]) or type(item["number"]) is not int
                or not 1 <= item["number"] <= 200 or not isinstance(item["prompt"], str)
                or len(item["prompt"]) > 4000 or (part > 2 and not item["prompt"].strip())
                or not isinstance(choices, list) or len(choices) != (3 if part == 2 else 4)
                or not all(nonempty(x) and len(x) <= 4000 for x in choices)
                or len({x.strip().casefold() for x in choices}) != len(choices)):
            raise ValueError("Invalid owner question or options")
    numbers = [item["number"] for item in items]
    if numbers != list(range(numbers[0], numbers[0] + len(items))):
        raise ValueError("Owner group numbers are not contiguous")
    ids = [item["id"] for item in items]
    passage = row.get("passage")
    if passage is not None and (not nonempty(passage) or len(passage) > 20000):
        raise ValueError("Invalid owner passage")
    extra = row.get("extraImages", [])
    if not isinstance(extra, list) or len(extra) > 3 or (extra and (not row.get("image") or part == 1)):
        raise ValueError("Invalid owner image sequence")
    required = {"audioItems": bool(row.get("audio")), "imageItems": bool(row.get("image")), "passageItems": bool(passage)}
    if (required["audioItems"] != (part <= 4) or (part == 1 and not required["imageItems"])
            or (required["imageItems"] and part in {2, 5}) or (passage and part < 6)
            or (part >= 6 and not (passage or required["imageItems"]))):
        raise ValueError("Missing or unexpected owner audio, photo or passage")
    if any(row.get(key, []) != (ids if present else []) for key, present in required.items()):
        raise ValueError("Owner media or passage does not match the ordered item IDs")
    for _, asset in group_assets(row):
        if (not isinstance(asset, dict) or set(asset) != {"path", "size", "sha256"}
                or not isinstance(asset["sha256"], str) or not SHA.fullmatch(asset["sha256"])
                or type(asset["size"]) is not int or not isinstance(asset["path"], str)):
            raise ValueError("Invalid owner media metadata")
        path = root / "media" / Path(asset["path"]).name
        if not path.is_file() or path.resolve().parent != (root / "media").resolve():
            raise ValueError("Owner media missing or outside the bundle")
    verify_media(row, root / "media", root / "media")


def check_disjoint(groups):
    def normalize(value):
        return " ".join(value.casefold().split())

    group_ids, question_ids, numbers, binaries, contexts = set(), set(), set(), set(), set()
    for group in groups:
        gid = group["id"]
        if gid in group_ids:
            raise ValueError("Duplicate group across practice or inventories")
        group_ids.add(gid)
        assets = tuple(asset["sha256"] for _, asset in group_assets(group))
        if len(set(assets)) != len(assets) or binaries.intersection(assets):
            raise ValueError("Duplicate media across practice or inventories")
        binaries.update(assets)
        for item in group["items"]:
            index = (group["source"], group["version"], item["number"])
            identity = (group["part"], normalize(group.get("passage") or ""), assets,
                        normalize(item["prompt"]), tuple(sorted(normalize(choice) for choice in item["choices"])))
            if item["id"] in question_ids or index in numbers or identity in contexts:
                raise ValueError("Duplicate question across practice or inventories")
            question_ids.add(item["id"])
            numbers.add(index)
            contexts.add(identity)


def owner_groups(root, previous, media):
    manifest = root / "bundle.json"
    if not manifest.is_file():
        check_disjoint(previous)
        return [], []
    bundle = read_json(manifest)
    if (not isinstance(bundle, dict) or set(bundle) != {"schema", "practice", "inventories"}
            or type(bundle["schema"]) is not int or bundle["schema"] != 1
            or not isinstance(bundle["practice"], list) or not isinstance(bundle["inventories"], list)):
        raise ValueError("Invalid owner bundle schema")
    inventory_ids, inventory_groups, used_versions = set(), [], set()
    quarantine = root.parent / "inventory-media"
    quarantine.mkdir(exist_ok=True)
    for inventory in bundle["inventories"]:
        if (not isinstance(inventory, dict) or inventory.keys() - {"id", "groups", "review"}
                or inventory.get("id") not in ("A", "B")
                or inventory["id"] in inventory_ids or not isinstance(inventory.get("groups"), list)):
            raise ValueError("Invalid owner inventory")
        inventory_ids.add(inventory["id"])
        for group in inventory["groups"]:
            validate_owner_group(group, root, used_versions)
            low = 1 if group["part"] == 1 else PART_ENDS[group["part"] - 2] + 1
            if any(not low <= item["number"] <= PART_ENDS[group["part"] - 1] for item in group["items"]):
                raise ValueError("Owner mock item is outside its Part")
        inventory_groups.extend(inventory["groups"])
    for group in bundle["practice"]:
        validate_owner_group(group, root, used_versions)
    check_disjoint(previous + bundle["practice"] + inventory_groups)
    for group in inventory_groups:
        verify_media(group, quarantine, root / "media")
    for group in bundle["practice"]:
        verify_media(group, media, root / "media")
    return bundle["practice"], bundle["inventories"]


def mock_form_review(review, digest, evidence, cache):
    if (not isinstance(review, dict) or review.get("status") != "APPROVED" or review.get("formSha256") != digest
            or not nonempty(review.get("reviewer")) or not nonempty(review.get("locator"))):
        return None
    try:
        stamp = review["reviewedAt"]
        if date.fromisoformat(stamp).isoformat() != stamp:
            return None
        source_host(review["evidenceUrl"])
    except (KeyError, TypeError, ValueError):
        return None
    if not evidence_matches(evidence, review.get("evidenceSha256"), cache):
        return None
    return {"status": "APPROVED", "evidence": f'{review["evidenceUrl"]}#{review["locator"]}'}


def release_mock_pair(inventories, active_groups, evidence):
    by_id = {entry["id"]: entry for entry in inventories}
    summary, ready, cache = {}, [], {}
    for slot in ("A", "B"):
        inventory = by_id.get(slot, {})
        groups = [active_groups[g["id"]] for g in inventory.get("groups", []) if g["id"] in active_groups]
        items = [item for group in groups for item in group["items"]]
        digest = sha256(json.dumps(groups, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        sourced = sum("sourceKey" in i for i in items)
        verified = sum(key.get("status") == "VERIFIED" and not key.get("batchAccepted") and not key.get("practiceOnly")
                       for item in items if (key := item.get("key")))
        status = "MISSING_INVENTORY"
        if inventory:
            status = "STRUCTURE_INCOMPLETE"
            if ([i["number"] for i in items] == list(range(1, 201))
                    and all(sum(len(g["items"]) for g in groups if g["part"] <= part) == end
                            for part, end in enumerate(PART_ENDS, 1))):
                status = "ITEM_REVIEW_REQUIRED"
                if sourced == verified == 200:
                    review = mock_form_review(inventory.get("review"), digest, evidence, cache)
                    status = "FORM_REVIEW_REQUIRED"
                    if review:
                        status = "FORM_READY"
                        ready.append({"id": slot, "version": digest, "groups": groups, "review": review})
        summary[slot] = {"available": len(items), "source_keys": sourced, "reviewed": verified,
                         "form_sha256": digest if groups else None, "status": status}
    return (ready if len(ready) == 2 else []), summary


def remove_inactive_mock_media(previous_pack, pack, media):
    retained = {asset["path"] for group in
                pack["practice"] + [g for form in pack.get("forms", []) for g in form["groups"]]
                for _, asset in group_assets(group)}
    for form in previous_pack.get("forms", []):
        for group in form["groups"]:
            for _, asset in group_assets(group):
                path = asset["path"]
                if path not in retained and re.fullmatch(r"study_pack/media/[0-9a-f]{64}\.(?:mp3|png|jpg)", path):
                    (media / Path(path).name).unlink(missing_ok=True)


def review_rows(rows, groups, evidence, *, strict=True):
    bindings = {item["id"]: (item_binding(group, item), tuple("ABCD"[:len(item["choices"])]))
                for group in groups for item in group["items"]}
    seen, locations, accepted, cache = set(), set(), [], {}
    for row in rows:
        try:
            item_id = row["itemId"]
            binding, labels = bindings[item_id]
            day = row["reviewedAt"]
            if (not isinstance(day, str) or date.fromisoformat(day).isoformat() != day
                    or row["status"] not in STATUSES or not nonempty(row["reviewer"]) or len(row["reviewer"]) > 100
                    or not nonempty(row["locator"]) or len(row["locator"]) > 240
                    or not valid_source(row, binding, labels, evidence, cache, source_host)):
                raise ValueError("Key or review lacks valid source binding, date or evidence")
            if (row.get("explanation") or row.get("explanationLocator")) and (
                    row["status"] != "APPROVED" or not nonempty(row.get("explanation"))
                    or not nonempty(row.get("explanationLocator")) or len(row["explanation"]) > 5000
                    or len(row["explanationLocator"]) > 240):
                raise ValueError("Explanation requires approval and source locator")
            location = (row["evidenceSha256"], row["locator"].strip().casefold())
        except (KeyError, TypeError, ValueError):
            if strict:
                raise ValueError("Invalid or stale review row") from None
            continue
        if item_id in seen or location in locations:
            raise ValueError("Duplicate reviewed item or evidence locator")
        seen.add(item_id)
        locations.add(location)
        accepted.append(row)
    return accepted


def publisher_key_rows(rows, groups, evidence):
    bindings = {item["id"]: (item_binding(group, item), tuple("ABCD"[:len(item["choices"])]))
                for group in groups for item in group["items"]}
    accepted, seen, locators, hashes = [], set(), set(), {}
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("itemId"), str):
            raise ValueError("Invalid publisher key row")
        item_id = row["itemId"]
        if item_id not in bindings or not valid_source(row, *bindings[item_id], evidence, hashes, source_host):
            raise ValueError("Publisher key does not match the item or evidence bytes")
        locator = (row["evidenceSha256"], row["locator"].strip().casefold())
        if item_id in seen or locator in locators:
            raise ValueError("Duplicate publisher key or evidence locator")
        seen.add(item_id)
        locators.add(locator)
        accepted.append(row)
    return accepted


def key_request_rows(groups, queue):
    """Project the pending queue into form rows bound to the current pack."""
    pending = {item["id"]: (group, item) for group in groups for item in group["items"] if not item.get("key")}
    ids = [row["itemId"] for row in queue]
    if len(ids) != len(set(ids)) or set(ids) != pending.keys():
        raise ValueError("Review queue does not match the pending items in the Study pack")
    requests = []
    for row in queue:
        group, item = pending[row["itemId"]]
        binding = item_binding(group, item)
        if (any(row.get(field) != value for field, value in binding.items())
                or row.get("part") != group["part"] or row.get("number") != item["number"]):
            raise ValueError("Review queue contains a stale question binding")
        requests.append({
            **binding, "part": group["part"], "number": item["number"], "orderedChoices": item["choices"],
            "queueStatus": row["status"], "status": "SOURCE_ONLY", "label": "", "evidenceUrl": group["source"],
            "evidenceSha256": "", "locator": "", "reviewer": "", "reviewedAt": "",
        })
    return sorted(requests, key=lambda row: (row["part"], row["source"], row["version"], row["number"], row["itemId"]))


def export_key_request(source=ROOT02, destination=ROOT02.parent / "content-03" / "key-request"):
    pack_path = source / "assets/study_pack/pack.json"
    digest = sha256(pack_path.read_bytes()).hexdigest()
    if digest != read_json(source / "activation.json")["pack_sha256"]:
        raise ValueError("Study pack differs from its activation receipt")
    pack = read_json(pack_path)
    queue = [row for row in read_json(source / "answer-review-queue.json") if "form" not in row]
    rows = key_request_rows(pack["practice"], queue)
    reading = [row for row in rows if row["part"] >= 5]
    listening = [row for row in rows if row["part"] < 5]
    destination.mkdir(parents=True, exist_ok=True)
    save_json(destination / "01-reading-key-request.json", reading)
    save_json(destination / "02-listening-key-request.json", listening)
    return {"pack_sha256": digest, "reading": len(reading), "listening": len(listening)}


def assemble(directory=ROOT02, *, review_file=None, evidence_files=()):
    base = seed_previous(directory)
    groups = base["practice"] + read_json(directory / "new-groups.json")
    media = directory / "assets/study_pack/media"
    media.mkdir(parents=True, exist_ok=True)
    for group in base["practice"]:
        verify_media(group, media, directory / "base-media")
    for group in groups[len(base["practice"]):]:
        verify_media(group, media, directory / "media")
    owner_staging = directory / "owner-practice-media"
    owner_staging.mkdir(exist_ok=True)
    extra, inventories = owner_groups(directory / "owner", groups, owner_staging)
    groups += extra
    groups.sort(key=lambda group: (group["part"], group["source"], group["version"], group["items"][0]["number"]))
    form_by_group = {group["id"]: form["id"] for form in inventories for group in form["groups"]}
    practice_ids = {item["id"] for group in groups for item in group["items"]}
    practice = groups.copy()
    groups.extend(group for form in inventories for group in form["groups"])
    evidence = directory / "source-evidence"
    evidence.mkdir(exist_ok=True)
    intake = directory / "review-decisions.json"
    existing = optional_rows(intake)
    for body_file in evidence_files:
        body = read_blob(body_file)
        (evidence / f"{sha256(body).hexdigest()}.bin").write_bytes(body)
    owner_rows = review_rows(optional_rows(directory / "owner/reviews.json"), groups, evidence)
    published = publisher_key_rows(optional_rows(directory / "owner/source-keys.json"), groups, evidence)
    if review_file:
        incoming = review_rows(optional_rows(review_file), groups, evidence)
        if not incoming:
            raise ValueError("Review export has no decisions")
        updated_ids = {row["itemId"] for row in incoming}
        merged = [row for row in existing if row["itemId"] not in updated_ids] + incoming
        review_rows(merged + owner_rows, groups, evidence)
        save_json(intake, merged)
        existing = merged
    decisions = review_rows(existing + owner_rows, groups, evidence, strict=False)
    published_ids = {row["itemId"] for row in published}
    candidates = published + [row for row in decisions
                              if row["itemId"] in practice_ids and row["itemId"] not in published_ids]
    found = {row["itemId"] for row in candidates}
    candidates += [row for row in source_keys(practice, snapshot_source(), evidence) if row["itemId"] not in found]
    # A review decision is independent from the source-key projection.
    source_fields = {"itemId", "groupId", "source", "version", "itemSha256", "label", "evidenceUrl",
                     "evidenceSha256", "locator"}
    keys = [{key: row[key] for key in sorted(source_fields)} for row in candidates]
    withdrawn = set(optional_rows(directory / "withdrawn-groups.json"))
    active, queue = activate_groups(groups, keys, decisions, evidence, withdrawn, source_host=source_host)
    forms, inventory_status = release_mock_pair(inventories, {group["id"]: group for group in active}, evidence)
    for row in queue:
        if row["groupId"] in form_by_group:
            row["form"] = form_by_group[row["groupId"]]
    practice = [group for group in active if group["id"] not in form_by_group]
    pack = {"schema": 1, "practice": practice}
    if forms:
        pack["forms"] = forms
    if len((json.dumps(pack, ensure_ascii=False, indent=2) + "\n").encode("utf-16-le")) // 2 > 1_000_000:
        raise ValueError("Study pack exceeds the Android manifest limit")
    extra_ids = {group["id"] for group in extra}
    for group in practice:
        if group["id"] in extra_ids:
            verify_media(group, media, owner_staging)
    for form in forms:
        for group in form["groups"]:
            verify_media(group, media, directory / "inventory-media")
    save_json(directory / "source-keys.json", keys)
    save_json(directory / "reviews.json", decisions)
    save_json(directory / "answer-review-queue.json", queue)
    target = media.parent / "pack.json"
    previous_pack = read_json(target) if target.is_file() else {}
    save_json(target, pack)
    remove_inactive_mock_media(previous_pack, pack, media)
    counts = {}
    for part in range(1, 8):
        items = [item for group in practice if group["part"] == part for item in group["items"]]
        counts[part] = {"available": len(items), "source_keys": sum("sourceKey" in item for item in items),
                        "reviewed": sum("key" in item for item in items)}
    report = {"counts": counts, "groups": len(practice), "queued": len(queue),
              "queue_status": dict(Counter(row["status"] for row in queue)),
              "decisions": dict(Counter(row["status"] for row in decisions)),
              "owner_items": sum(len(group["items"]) for group in extra),
              "quarantined_forms": {f["id"]: sum(len(g["items"]) for g in f["groups"]) for f in inventories if not forms},
              "mock_inventory": inventory_status, "published_forms": [form["id"] for form in forms],
              "pack_sha256": sha256(target.read_bytes()).hexdigest()}
    write_json(directory / "activation.json", report)
    from study_review_page import render_review
    render_review(directory / "review.html", active, queue, decisions, form_by_group=form_by_group)
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--import-review", type=Path)
    parser.add_argument("--evidence", action="append", type=Path, default=[], help="Attach original local evidence file")
    parser.add_argument("--export-key-request", action="store_true", help="Export pending Reading and Listening rows without rebuilding")
    parser.add_argument("--workspace", default=ROOT02.name, help="Private content-NN directory under Study tooling")
    args = parser.parse_args()
    folder = ROOT02.parent / args.workspace
    if not re.fullmatch(r"content-[0-9]{2}", args.workspace) or folder.resolve() != folder:
        parser.error("Select a local content-NN workspace")
    if args.export_key_request:
        if args.import_review or args.evidence:
            parser.error("Export and evidence import are separate operations")
        report = export_key_request() if folder == ROOT02 else export_key_request(folder, folder / "key-request")
    else:
        report = assemble(folder, review_file=args.import_review, evidence_files=args.evidence)
    print(json.dumps(report, ensure_ascii=False))
