#!/usr/bin/env python3
"""Project one bounded practice batch into the private Study asset directory."""
import argparse
from hashlib import sha256
import html
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

from crawl_one_zenlish_part3_group import (
    PAGE, PageMarkup, embedded_documents, json_objects_matching, normalize_questions, plain_text,
)
from listening_http import BoundedClient, FetchError
from listening_manifest import Validator, choose_file, read_blob, read_json
from listening_media import inspect_media

TOOLING = Path(__file__).resolve().parents[1] / ".tooling"
SOURCE = TOOLING / "listening-overnight"
ROOT = TOOLING / "two-user-study"
# Only these five records from the stored page may enter this batch.
READING = ((5, 41137, (101,)), (5, 41140, (102,)), (5, 41141, (103,)),
           (6, 41199, (131, 132, 133, 134)), (7, 41211, (147, 148)))


def reading_record(snapshot, group_id, part, numbers):
    marker = re.compile(r'"question_id"\s*:\s*' + str(group_id) + r'\b')
    matches = []
    for source in embedded_documents(snapshot, str(group_id), "question_id"):
        for item in json_objects_matching(source, marker):
            if item.get("question_id") == group_id and "sub_questions" in item and item not in matches:
                matches.append(item)
    if len(matches) != 1:
        raise ValueError("Missing or ambiguous Reading group")
    record = matches[0]
    if record.get("type") != "reading" or record.get("is_grouped") != (part in (6, 7)):
        raise ValueError("Wrong Reading group type")
    markup = html.unescape(record.get("content", ""))
    parsed = PageMarkup()
    parsed.feed(markup)
    text = plain_text(markup)
    if len(parsed.images) > 1 or (part > 5 and not (parsed.images or text)):
        raise ValueError("Missing context or unsupported multi-image passage")
    if parsed.images:
        path = urlsplit(parsed.images[0])
        if (path.scheme, path.netloc) != ("https", "zenlishtoeic.vn") or not path.path.startswith("/wp-content/uploads/"):
            raise ValueError("Passage image outside the source media path")
    questions = normalize_questions(record, PAGE, part=part, indices=numbers)
    return questions, text or None, parsed.images[0] if parsed.images else None


def project_items(questions):
    return [
        {
            "id": item["id"],
            "number": item["index"],
            "prompt": re.sub(r"^\s*\d+[.):]\s*", "", item["prompt"] or ""),
            "choices": [text or label for label, text in sorted(item["choices"].items())],
        }
        for item in questions
    ]


def package_media(payload, folder, expected_kind):
    info = inspect_media(payload)
    if not info["mime"].startswith(expected_kind + "/"):
        raise ValueError("Unexpected media kind")
    suffix = {"mp3": "mp3", "png": "png", "jpeg": "jpg"}[info["format"]]
    name = f'{info["sha256"]}.{suffix}'
    (folder / name).write_bytes(payload)
    return {"path": f"study_pack/media/{name}", "size": len(payload), "sha256": info["sha256"]}


def prepare(fetch_images):
    snapshot = (SOURCE / "zenlish-p3-q32-34/source_page.html").read_bytes()
    version = sha256(snapshot).hexdigest()
    source = read_json(SOURCE / "normalized_manifest.json")
    if Validator(SOURCE).validate(source)["errors"]:
        raise ValueError("Listening structural validation failed")
    target = ROOT / "assets/study_pack"
    media = target / "media"
    media.mkdir(parents=True, exist_ok=True)
    cache = ROOT / "reading-cache"
    cache.mkdir(exist_ok=True)
    groups, omissions = [], []
    for group in source["groups"]:
        if group["qa"]["status"] == "REJECTED" or group["source"]["snapshot_sha256"] != version:
            raise ValueError("Listening group rejected or from a different snapshot")
        questions = group["questions"]
        audio = package_media(read_blob(choose_file(SOURCE.resolve(), group["audio"]["path"])), media, "audio")
        photo = questions[0].get("image")
        image = package_media(read_blob(choose_file(SOURCE.resolve(), photo["path"])), media, "image") if photo else None
        items = project_items(questions)
        groups.append({"id": group["id"], "part": group["part"], "version": version, "source": PAGE,
                       "audio": audio, "image": image, "audioItems": group["audio"]["item_ids"], "items": items})
    client = BoundedClient()
    for part, id_number, numbers in READING:
        try:
            questions, text, image_url = reading_record(snapshot.decode("utf-8-sig"), id_number, part, numbers)
            image = None
            if image_url:
                cached = cache / (sha256(image_url.encode()).hexdigest() + ".png")
                if not cached.exists() and fetch_images:
                    response = client.get(image_url, limit=2 * 1024**2, accept="image/png,image/jpeg")
                    if response.status != 200 or response.content_type not in ("image/png", "image/jpeg"):
                        raise ValueError("Source did not return the required passage image")
                    image = package_media(response.body, media, "image")
                    cached.write_bytes(response.body)
                if image is None:
                    image = package_media(read_blob(cached, 2 * 1024**2), media, "image")
            groups.append({"id": f"zenlish:{id_number}", "part": part, "version": version, "source": PAGE,
                           "passage": text, "image": image, "items": project_items(questions)})
        except (FetchError, ValueError, OSError) as error:
            omissions.append({"part": part, "group": id_number, "reason": str(error)})
    # Remove stale media from previous outputs using only direct children of the generated directory.
    allowed = {Path(asset["path"]).name for group in groups for asset in (group.get("audio"), group.get("image")) if asset}
    for asset_file in media.iterdir():
        if asset_file.is_file() and asset_file.name not in allowed and re.fullmatch(r"[0-9a-f]{64}\.(mp3|png|jpg)", asset_file.name):
            asset_file.unlink()
    staged = target / "pack.json.tmp"
    staged.write_text(json.dumps({"schema": 1, "practice": groups}, ensure_ascii=False), encoding="utf-8")
    staged.replace(target / "pack.json")
    result = {"source_version": version, "counts": {part: sum(len(g["items"]) for g in groups if g["part"] == part)
               for part in range(1, 8)}, "groups": len(groups), "verified_keys": 0, "http_requests": client.requests,
              "http_downloaded": client.downloaded, "issues": omissions}
    (ROOT / "batch.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch-reading-images", action="store_true")
    prepare(parser.parse_args().fetch_reading_images)
