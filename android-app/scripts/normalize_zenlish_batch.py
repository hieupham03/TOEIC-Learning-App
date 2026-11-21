#!/usr/bin/env python3
"""Convert this local Zenlish receipt to an offline, website-independent manifest."""
from hashlib import sha256
import json
from pathlib import Path
import sys
from urllib.parse import urlsplit

sys.dont_write_bytecode = True
from crawl_one_zenlish_part3_group import AUDIO, MAX_PAGE, ROOT, extract_group, normalize_questions
from crawl_zenlish_representative_groups import TARGETS, load_group
from listening_manifest import choose_file, read_blob, read_json


def text_id(value):
    return str(value) if value is not None else None


def local_asset(record, folder, *, identifier, group_id):
    if record is None:
        return None
    private_file = choose_file(folder, record["path"])
    return {**{key: record[key] for key in ("bytes", "sha256", "mime", "format")},
            "id": identifier, "group_id": group_id, "source_url": record["url"],
            "path": private_file.relative_to(ROOT).as_posix()}


def normalize(batch, snapshot, page):
    text = snapshot.decode("utf-8-sig")
    snapshot_hash = sha256(snapshot).hexdigest()
    if snapshot_hash != page["sha256"] or len(snapshot) != page["bytes"]:
        raise ValueError("Page receipt and stored bytes disagree")
    if not 1 <= len(batch["groups"]) <= 4:
        raise ValueError("Invalid batch group count")
    groups = []
    for receipt in sorted(batch["groups"], key=lambda g: g["part"]):
        part = receipt["part"]
        if not receipt.get("groups"):
            continue  # Per-part stopped or absent records remain in the batch receipt.
        group_id = "zenlish:" + receipt["group_id"]
        if receipt["source"] != "zenlishtoeic.vn" or receipt["page"]["sha256"] != snapshot_hash:
            raise ValueError("Group receipt and page snapshot disagree")
        if part == 3:
            folder = ROOT / "zenlish-p3-q32-34"
            items = normalize_questions(extract_group(text, page["url"]), page["url"])
            audio_url, image_url = AUDIO, None
        else:
            folder = ROOT / f"representative-continuation/part-{part}"
            target = next(target for target in TARGETS if target[0] == part)
            items, audio_url, image_url = load_group(text, page["url"], target)
        if len(items) != receipt["questions"] or [q["index"] for q in items] != receipt["question_indices"]:
            raise ValueError("Question receipt and saved page disagree")
        audio_id = group_id + ":" + urlsplit(audio_url).path.rsplit("/", 1)[-1]
        raw_audio = receipt.get("audio")
        audio = local_asset(raw_audio, folder, identifier=audio_id, group_id=group_id)
        if audio is not None:
            if urlsplit(audio["source_url"]).path.rsplit("/", 1)[-1] != urlsplit(audio_url).path.rsplit("/", 1)[-1]:
                raise ValueError("Committed receipt refers to a different audio file")
            audio.update({key: raw_audio[key] for key in ("sample_rate_hz", "channels", "duration_seconds",
                                                         "duration_method", "decode_status", "probe_status")})
            audio.update(item_ids=[q["id"] for q in items], requested_url=audio_url)
        questions = []
        for row in items:
            img = receipt.get("image")
            image = None
            if img and img["question_id"] == row["id"]:
                if not image_url or row["image_source_url"] != image_url:
                    raise ValueError("Image association absent in the stored page")
                if urlsplit(img["url"]).path.rsplit("/", 1)[-1] != urlsplit(image_url).path.rsplit("/", 1)[-1]:
                    raise ValueError("Image receipt names a different asset")
                image = local_asset(img, folder, identifier=row["id"] + ":image", group_id=group_id)
                image["item_id"] = row["id"]
            answer = row["answer"]
            questions.append({"id": row["id"], "source_item_id": text_id(row["source_item_id"]),
                              "group_id": group_id, "index": row["index"], "presentation": row["presentation"],
                              "prompt": row["prompt"], "choices": row["choices"],
                              "answer": {"label": answer["label"], "status": answer["status"],
                                         "evidence": answer["evidence_url"]},
                              "image": image, "image_required": part == 1})
        groups.append({"id": group_id, "source_group_id": receipt["group_id"], "part": part,
                       "sequence": len(groups) + 1, "retrieval_status": receipt["status"],
                       "expected_indices": receipt["expected_indices"], "questions": questions,
                       "source": {"site": receipt["source"], "page_url": page["url"],
                                  "snapshot_path": "zenlish-p3-q32-34/source_page.html",
                                  "snapshot_sha256": snapshot_hash, "version": "sha256:" + snapshot_hash,
                                  "retrieved_at_utc": receipt["retrieved_at_utc"]},
                       "audio_binding": {"id": audio_id, "url": audio_url}, "audio": audio,
                       "qa": {"status": "NOT_RUN", "evidence": None},
                       "rights": {"status": "PO_DECLARED_NOT_INSPECTED", "evidence": None}})
    return {"schema_version": 1, "groups": groups}


def main():
    if ROOT.resolve() != ROOT:
        raise ValueError("Local evidence directory must not be redirected")
    batch = read_json(choose_file(ROOT, "representative-continuation/batch.json"))
    p3 = read_json(choose_file(ROOT, "zenlish-p3-q32-34/acquisition.json"))
    page = p3["page"]
    snapshot = read_blob(choose_file(ROOT, "zenlish-p3-q32-34/source_page.html"), MAX_PAGE)
    document = normalize(batch, snapshot, page)
    output = ROOT / "normalized_manifest.json"
    data = (json.dumps(document, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    if output.exists():
        if output.resolve() != output or output.read_bytes() != data:
            raise ValueError("Existing normalized manifest differs; preserve the evidence")
    else:
        with output.open("xb") as stream:
            stream.write(data)
    print(f"Normalized {len(document['groups'])} group(s) offline. No readiness changed.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, TypeError, KeyError, StopIteration, RecursionError):
        sys.exit("Offline normalization failed. Inspect the private declarations and receipt paths.")
