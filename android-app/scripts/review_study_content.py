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
    SHA, activate_groups, group_assets, item_binding, nonempty, optional_rows, source_keys, valid_source, verify_media,
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
        if (not isinstance(inventory, dict) or set(inventory) != {"id", "groups"} or inventory["id"] not in ("A", "B")
                or inventory["id"] in inventory_ids or not isinstance(inventory["groups"], list)):
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
    evidence = directory / "source-evidence"
    evidence.mkdir(exist_ok=True)
    intake = directory / "review-decisions.json"
    existing = optional_rows(intake)
    for body_file in evidence_files:
        body = read_blob(body_file)
        (evidence / f"{sha256(body).hexdigest()}.bin").write_bytes(body)
    owner_rows = review_rows(optional_rows(directory / "owner/reviews.json"), groups, evidence)
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
    decided = {row["itemId"] for row in decisions}
    candidates = decisions + [row for row in source_keys(groups, snapshot_source(), evidence) if row["itemId"] not in decided]
    # A review decision is independent from the source-key projection.
    source_fields = {"itemId", "groupId", "source", "version", "itemSha256", "label", "evidenceUrl",
                     "evidenceSha256", "locator"}
    keys = [{key: row[key] for key in sorted(source_fields)} for row in candidates]
    withdrawn = set(optional_rows(directory / "withdrawn-groups.json"))
    active, queue = activate_groups(groups, keys, decisions, evidence, withdrawn, source_host=source_host)
    pack = {"schema": 1, "practice": active}
    if len((json.dumps(pack, ensure_ascii=False, indent=2) + "\n").encode("utf-16-le")) // 2 > 1_000_000:
        raise ValueError("Study pack exceeds the Android manifest limit")
    extra_ids = {group["id"] for group in extra}
    for group in active:
        if group["id"] in extra_ids:
            verify_media(group, media, owner_staging)
    save_json(directory / "source-keys.json", keys)
    save_json(directory / "reviews.json", decisions)
    save_json(directory / "answer-review-queue.json", queue)
    target = media.parent / "pack.json"
    save_json(target, pack)
    counts = {}
    for part in range(1, 8):
        items = [item for group in active if group["part"] == part for item in group["items"]]
        counts[part] = {"available": len(items), "source_keys": sum("sourceKey" in item for item in items),
                        "reviewed": sum("key" in item for item in items)}
    report = {"counts": counts, "groups": len(active), "queued": len(queue),
              "queue_status": dict(Counter(row["status"] for row in queue)),
              "decisions": dict(Counter(row["status"] for row in decisions)),
              "owner_items": sum(len(group["items"]) for group in extra),
              "quarantined_forms": {f["id"]: sum(len(g["items"]) for g in f["groups"]) for f in inventories},
              "pack_sha256": sha256(target.read_bytes()).hexdigest()}
    write_json(directory / "activation.json", report)
    from study_review_page import render_review
    render_review(directory / "review.html", active, queue, decisions)
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--import-review", type=Path)
    parser.add_argument("--evidence", action="append", type=Path, default=[], help="Attach original local evidence file")
    args = parser.parse_args()
    print(json.dumps(assemble(review_file=args.import_review, evidence_files=args.evidence), ensure_ascii=False))
