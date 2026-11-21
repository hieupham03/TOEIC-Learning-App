#!/usr/bin/env python3
"""One continuation for three targeted groups discovered in the saved Zenlish page."""
from datetime import datetime, timezone
from hashlib import sha256
import html
import json
from pathlib import Path
import re
import sys
from urllib.parse import urljoin, urlsplit

sys.dont_write_bytecode = True
from crawl_one_zenlish_part3_group import (
    MAX_PAGE, ROOT, PageMarkup, check_audio, embedded_documents, json_objects_matching,
    normalize_questions, page_restricted, source_integer,
)
from listening_http import BoundedClient, FetchError, MAX_BYTES, MAX_MEDIA, MAX_REQUESTS, approved_host
from listening_media import inspect_media, probe_audio

# Only metadata observed in the already acquired public HTML. These are
# selectors, not inferred media URLs.
TARGETS = (
    (1, 40911, (1,), "zenlish-test-01-part-1-1.mp3"),
    (2, 40943, (7,), "zenlish-test-01-part-2-7.mp3"),
    (4, 41104, (71, 72, 73), "zenlish-test-01-part-4-71-73.mp3"),
)


def load_group(text, page, target):
    part, group_id, indices, clip = target
    marker = re.compile(r'"audio_url"\s*:\s*"[^"]*' + re.escape(clip) + r'"')
    candidates = []
    for source in embedded_documents(text, clip, "audio_url"):
        for group in json_objects_matching(source, marker):
            audio = group.get("audio_url")
            if (source_integer(group.get("question_id")) == group_id and isinstance(audio, str)
                    and urlsplit(audio).path.rsplit("/", 1)[-1] == clip and group not in candidates):
                candidates.append(group)
    if len(candidates) != 1:
        raise ValueError("Expected one group bound to the specified audio ID")
    group = candidates[0]
    if group.get("is_grouped") is not (part == 4):
        raise ValueError("Unexpected source grouping flag")
    for key in ("part", "part_number"):
        if key in group and source_integer(group[key]) != part:
            raise ValueError("Source declares a different Part")
    audio_url = urljoin(page, group["audio_url"])
    if approved_host(audio_url) != "zenlishtoeic.vn":
        raise FetchError("Audio host differs from approved page host", blocked=True)
    questions = normalize_questions(group, page, part=part, indices=indices)
    image_urls = {item["image_source_url"] for item in questions if item["image_source_url"]}
    for content in (group.get("content"), *(q.get("title") for q in group["sub_questions"])):
        if isinstance(content, str):
            markup = PageMarkup()
            markup.feed(html.unescape(content))
            markup.close()
            image_urls.update(urljoin(page, image) for image in markup.images)
    if len(image_urls) > 1 or (image_urls and part != 1):
        raise ValueError("Image assignment is ambiguous")
    image = next(iter(image_urls), None)
    if image and approved_host(image) != "zenlishtoeic.vn":
        raise FetchError("Image host differs from approved page host", blocked=True)
    if part == 1 and image:
        questions[0]["image_source_url"] = image
    return questions, audio_url, image


def inspect_access(response):
    if response.content_type in {"text/html", "application/xhtml+xml"}:
        text = response.body.decode("utf-8", errors="replace")
        markup = PageMarkup()
        markup.feed(text)
        if page_restricted(text, markup):
            raise FetchError("Media endpoint returned an access interstitial", blocked=True)


def get_target(text, page, target, output, client):
    part, group_id, indices, _ = target
    result = {"part": part, "group_id": str(group_id), "expected_indices": list(indices), "groups": 0,
              "questions": 0, "status": "PARTIAL", "source": "zenlishtoeic.vn", "page": page,
              "rights_status": "PO_DECLARED_NOT_INSPECTED", "qa_status": "NOT_RUN",
              "retrieved_at_utc": datetime.now(timezone.utc).isoformat(), "errors": []}
    try:
        questions, audio_url, image_url = load_group(text, page["url"], target)
        result.update(groups=1, questions=len(questions), question_indices=[q["index"] for q in questions],
                      source_question_ids=[q["source_item_id"] for q in questions],
                      explicit_answer_count=sum(q["answer"]["status"] == "SOURCE_EXPLICIT" for q in questions))
        (output / "questions.json").write_text(json.dumps(questions, ensure_ascii=False, indent=2), encoding="utf-8")
        audio = client.get(audio_url, limit=MAX_MEDIA, accept="audio/mpeg, application/octet-stream")
        inspect_access(audio)
        meta = check_audio(audio, audio_url)
        audio_path = output / "audio.mp3"
        audio_path.write_bytes(audio.body)
        result["audio"] = dict(meta, **probe_audio(audio_path), url=audio.url, path=audio_path.name,
                               response_status=audio.status, declared_mime=audio.content_type)
        if "FAIL" in {result["audio"]["decode_status"], result["audio"]["probe_status"]}:
            result["errors"].append("Local codec tool reported failure")
        if image_url:
            image = client.get(image_url, limit=MAX_MEDIA, accept="image/png, image/jpeg")
            inspect_access(image)
            if urlsplit(image.url).path.rsplit("/", 1)[-1] != urlsplit(image_url).path.rsplit("/", 1)[-1]:
                raise ValueError("Redirected image no longer matches the item's named image")
            meta = inspect_media(image.body)
            if meta["mime"] not in {"image/png", "image/jpeg"} or image.content_type != meta["mime"]:
                raise ValueError("Image media and declared MIME differ")
            image_path = output / ("photo." + meta["format"])
            image_path.write_bytes(image.body)
            result["image"] = dict(meta, url=image.url, path=image_path.name, response_status=image.status,
                                   declared_mime=image.content_type, question_id=questions[0]["id"])
        elif part == 1:
            result["errors"].append("Required Part 1 image link missing")
        if any(q["presentation"] == "SOURCE_LABELS_ONLY" for q in questions):
            result["errors"].append("Source provides choice labels only; no separately supplied stem/choice text")
        if not result["errors"]:
            result["status"] = "FETCHED"
    except FetchError as error:
        result["errors"].append(str(error))
        result["source_stopped"] = error.blocked
        if error.blocked and not result["groups"]:
            result["status"] = "BLOCKED"
    except (ValueError, RecursionError) as error:
        result["errors"].append(str(error))
    (output / "acquisition.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


def main():
    if ROOT.resolve() != ROOT:
        raise SystemExit("Local evidence directory must not be redirected")
    p3 = ROOT / "zenlish-p3-q32-34"
    output = ROOT / "representative-continuation"
    if p3.resolve() != p3 or output.resolve() != output:
        raise SystemExit("Local evidence directory must not be redirected")
    receipt = json.loads((p3 / "acquisition.json").read_text(encoding="utf-8"))
    page = receipt["page"]
    size = (p3 / "source_page.html").stat().st_size
    if (receipt["status"] != "FETCHED" or receipt.get("source_stopped") or receipt["group_id"] != "41021"
            or receipt["questions"] != 3 or receipt["http_requests"] >= MAX_REQUESTS
            or receipt["downloaded_bytes"] >= MAX_BYTES or size > MAX_PAGE
            or receipt["http_requests"] != len(receipt["request_audit"])
            or approved_host(page["url"]) != "zenlishtoeic.vn"):
        raise SystemExit("Previous acquisition was not eligible for continuation")
    raw = (p3 / "source_page.html").read_bytes()
    if len(raw) != page["bytes"] or sha256(raw).hexdigest() != page["sha256"]:
        raise SystemExit("Prior page hash or byte count mismatch")
    text = raw.decode("utf-8-sig")
    # This directory is reserved once. An interrupted run preserves the
    # evidence instead of silently starting another batch.
    output.mkdir(exist_ok=False)
    client = BoundedClient()
    client.requests = receipt["http_requests"]
    client.downloaded = receipt["downloaded_bytes"]
    client.audit = receipt["request_audit"].copy()
    client.last_start["zenlishtoeic.vn"] = client.now()
    groups = [receipt]
    for target in TARGETS:
        part = target[0]
        if any(group.get("source_stopped") for group in groups):
            groups.append({"part": part, "status": "NOT_RUN", "groups": 0, "questions": 0})
            continue
        folder = output / f"part-{part}"
        folder.mkdir()
        groups.append(get_target(text, page, target, folder, client))
    summary = {"groups": groups, "http_requests": client.requests, "downloaded_bytes": client.downloaded,
               "request_audit": client.audit}
    (output / "batch.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    compact = sorted((g["part"], g["status"], g["questions"]) for g in groups)
    print(f"Parts (part, status, questions) {compact}; {client.requests} requests; {client.downloaded} body bytes")
    return 0 if all(group["status"] == "FETCHED" for group in groups) else 2


if __name__ == "__main__":
    sys.exit(main())
