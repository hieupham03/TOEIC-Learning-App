"""Rebuild the private Study pack and answer-review queue without HTTP."""
import argparse
from collections import defaultdict
from hashlib import sha256
from pathlib import Path
import re

from acquire_study_content import BATCH, parse_study_record, snapshot_groups, write_json
from listening_http import MAX_MEDIA, approved_host
from listening_manifest import read_json
from listening_media import inspect_media
from prepare_study_pack import ROOT, SOURCE, project_items

SHA = re.compile(r"[0-9a-f]{64}")


def item_binding(group, item):
    fields = [group["id"], group["source"], group["version"], str(group["part"]),
              item["id"], str(item["number"]), item["prompt"], group.get("passage") or "",
              *((group.get(kind) or {}).get("sha256", "") for kind in ("audio", "image")), *item["choices"]]
    if group.get("extraImages"):
        fields += ["extraImages", *(asset["sha256"] for asset in group["extraImages"])]
    digest = sha256()
    for field in fields:
        raw = field.encode("utf-8")
        digest.update(str(len(raw)).encode("ascii") + b":" + raw)
    return {"groupId": group["id"], "itemId": item["id"], "source": group["source"],
            "version": group["version"], "itemSha256": digest.hexdigest()}


def by_item(records):
    result = defaultdict(list)
    for row in records:
        if not isinstance(row, dict) or not isinstance(row.get("itemId"), str):
            raise ValueError("Expected local ledger rows with itemId")
        result[row["itemId"]].append(row)
    return result


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def evidence_matches(evidence_dir, digest, cache):
    if not isinstance(digest, str) or not SHA.fullmatch(digest):
        return False
    if digest not in cache:
        path = evidence_dir / f"{digest}.bin"
        try:
            cache[digest] = (path.resolve().parent == evidence_dir.resolve() and 0 < path.stat().st_size <= MAX_MEDIA
                             and sha256(path.read_bytes()).hexdigest() == digest)
        except OSError:
            cache[digest] = False
    return cache[digest]


def valid_source(row, binding, labels, evidence_dir, cache, source_host=approved_host):
    digest = row.get("evidenceSha256")
    if (any(row.get(field) != value for field, value in binding.items()) or row.get("label") not in labels
            or not nonempty(row.get("locator"))):
        return False
    try:
        if source_host(row.get("evidenceUrl", "")) != source_host(binding["source"]):
            return False
        return evidence_matches(evidence_dir, digest, cache)
    except (TypeError, ValueError):
        return False


def activate_groups(groups, candidates, reviews, evidence_dir, withdrawn_ids, *, source_host=approved_host):
    source_rows, review_rows = by_item(candidates), by_item(reviews)
    group_ids = [group["id"] for group in groups]
    item_ids = [item["id"] for group in groups for item in group["items"]]
    if len(set(group_ids)) != len(group_ids) or len(set(item_ids)) != len(item_ids):
        raise ValueError("Duplicate Study group or item ID")
    media = [asset["sha256"] for group in groups for _, asset in group_assets(group)]
    if len(set(media)) != len(media):
        raise ValueError("Duplicate Study media")
    if withdrawn_ids - set(group_ids):
        raise ValueError("Withdrawal refers to an unknown group ID")
    active, queue, cache = [], [], {}
    for group in groups:
        if group["id"] in withdrawn_ids:
            continue
        items = []
        for base in group["items"]:
            item = {key: base[key] for key in ("id", "number", "prompt", "choices")}
            binding = item_binding(group, item)
            choices = tuple("ABCD"[:len(item["choices"])])
            source = source_rows.get(item["id"], [])
            review = review_rows.get(item["id"], [])
            status = "SOURCE_EVIDENCE_REQUIRED"
            if len(source) == 1 and valid_source(source[0], binding, choices, evidence_dir, cache, source_host):
                candidate = source[0]
                label = candidate["label"]
                choice = choices.index(label)
                proof = {**binding, "choice": choice, "evidenceSha256": candidate["evidenceSha256"]}
                item["sourceKey"] = proof
                status = "AWAITING_REVIEW"
                if (len(review) == 1 and review[0].get("status") == "APPROVED"
                        and nonempty(review[0].get("reviewer"))
                        and all(review[0].get(field) == candidate[field]
                                for field in (*binding, "label", "evidenceSha256", "evidenceUrl", "locator"))):
                    approval = review[0]
                    item["key"] = {**proof, "status": "VERIFIED", "reviewer": approval["reviewer"],
                                   "evidence": f'{candidate["evidenceUrl"]}#{candidate["locator"]}'}
                    if approval.get("reviewScope") == "PO_BATCH_ACCEPTANCE":
                        item["key"]["batchAccepted"] = True
                    if nonempty(approval.get("explanation")) and nonempty(approval.get("explanationLocator")):
                        item["key"]["explanation"] = approval["explanation"]
                elif len(review) == 1 and review[0].get("status") == "REVOKED":
                    status = "REVOKED"
                elif review and review[0].get("status") != "SOURCE_ONLY":
                    status = "REVIEW_REJECTED_OR_MISMATCH"
            elif source:
                status = "SOURCE_EVIDENCE_REJECTED"
            if "key" not in item:
                queue.append({**binding, "part": group["part"], "number": item["number"], "status": status,
                              "candidate": source[0] if len(source) == 1 else None})
            items.append(item)
        active.append({**group, "items": items})
    return active, queue


def source_keys(groups, snapshot, evidence_dir):
    version = sha256(snapshot).hexdigest()
    records = snapshot_groups(snapshot.decode("utf-8-sig"))
    rows = []
    for group in groups:
        record = records.get(group["id"].partition(":")[2])
        if group["version"] != version or record is None:
            continue
        try:
            part, questions, *_ = parse_study_record(record)
        except ValueError:
            continue
        if part != group["part"] or project_items(questions) != group["items"]:
            continue
        for question, item in zip(questions, group["items"]):
            label = question["answer"]["label"]
            if label:
                rows.append({**item_binding(group, item), "label": label, "evidenceUrl": group["source"],
                             "evidenceSha256": version, "locator": f'Snapshot group {group["id"]} item {item["number"]}'})
    if rows:
        (evidence_dir / f"{version}.bin").write_bytes(snapshot)
    return rows


def group_assets(group):
    yield from ((kind, group[kind]) for kind in ("audio", "image") if group.get(kind))
    yield from (("image", asset) for asset in group.get("extraImages", ()))


def verify_media(group, old_media, new_media):
    for kind, asset in group_assets(group):
        formats = ("mp3",) if kind == "audio" else ("png", "jpeg")
        name = Path(asset["path"]).name
        path = new_media / name
        if not path.is_file():
            path = old_media / name
        if not 0 < path.stat().st_size <= MAX_MEDIA:
            raise ValueError("Invalid media length")
        payload = path.read_bytes()
        metadata = inspect_media(payload)
        ext = "jpg" if metadata["format"] == "jpeg" else metadata["format"]
        if (metadata["format"] not in formats or len(payload) != asset["size"]
                or metadata["sha256"] != asset["sha256"]
                or asset["path"] != f'study_pack/media/{asset["sha256"]}.{ext}'):
            raise ValueError("Content media differs from the recorded asset")
        destination = old_media / name
        if path != destination and (not destination.is_file() or destination.read_bytes() != payload):
            destination.write_bytes(payload)


def optional_rows(path):
    if not path.is_file():
        return []
    rows = read_json(path)
    if not isinstance(rows, list):
        raise ValueError(f"{path.name} must contain a JSON array")
    return rows


def activate():
    original = read_json(BATCH / "base-pack.json")
    groups = original["practice"] + read_json(BATCH / "new-groups.json")
    target = ROOT / "assets/study_pack"
    evidence = BATCH / "source-evidence"
    evidence.mkdir(exist_ok=True)
    snapshot = (SOURCE / "zenlish-p3-q32-34/source_page.html").read_bytes()
    if sha256(snapshot).hexdigest() != read_json(BATCH / "acquisition.json")["source_version"]:
        raise ValueError("Saved Study snapshot differs from the acquisition receipt")
    candidates = source_keys(groups, snapshot, evidence) + optional_rows(BATCH / "source-keys.json")
    reviews = optional_rows(BATCH / "reviews.json")
    active, queue = activate_groups(groups, candidates, reviews, evidence, set(optional_rows(BATCH / "withdrawn-groups.json")))
    for group in active:
        verify_media(group, target / "media", BATCH / "media")
    write_json(BATCH / "answer-review-queue.json", queue)
    counts = {}
    for part in range(1, 8):
        items = [item for group in active if group["part"] == part for item in group["items"]]
        counts[part] = {"available": len(items), "source_keys": sum("sourceKey" in item for item in items),
                        "reviewed": sum("key" in item for item in items)}
    staged = target / "pack.json.tmp"
    write_json(staged, {**original, "practice": active})
    staged.replace(target / "pack.json")
    report = {"counts": counts, "total_groups": len(active), "queued": len(queue),
              "pack_sha256": sha256((target / "pack.json").read_bytes()).hexdigest()}
    write_json(BATCH / "activation.json", report)
    return report


if __name__ == "__main__":
    import json

    argparse.ArgumentParser(description=__doc__).parse_args()
    print(json.dumps(activate(), ensure_ascii=False))
