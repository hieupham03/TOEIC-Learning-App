"""Acquire one bounded extension from the approved public Study sources."""
import argparse
from collections import Counter
from hashlib import sha256
import html
import json
import re
from urllib.parse import urljoin, urlsplit

from crawl_one_zenlish_part3_group import (
    MAX_PAGE, PAGE, PageMarkup, check_audio, embedded_documents, normalize_questions,
    page_restricted, plain_text, source_integer,
)
from crawl_zenlish_representative_groups import inspect_access
from listening_http import BoundedClient, FetchError, MAX_MEDIA, approved_host
from listening_manifest import read_json
from listening_media import inspect_media
from prepare_study_pack import ROOT, SOURCE, package_media, project_items

BATCH = ROOT / "content-01"
MAX_GROUPS, MAX_QUESTIONS = 40, 120
PART_ENDS = (6, 31, 70, 100, 130, 146, 200)
PART_TARGETS = (4, 6, 5, 5, 9, 3, 8)
SOURCE_PAGES = (
    "https://test.thetoeiclab.vn/",
    "https://study4.com/tests/toeic/",
)


def snapshot_groups(text):
    groups = {}
    for document in embedded_documents(text, '"question_id"', "question_id"):
        for marker in re.finditer(r'"questions"\s*:\s*(?=\{)', document):
            try:
                records, _ = json.JSONDecoder().raw_decode(document, marker.end())
            except ValueError:
                continue
            for group_id, row in records.items():
                if not isinstance(row, dict) or source_integer(group_id) != source_integer(row.get("question_id")):
                    raise ValueError("Study record has an inconsistent source ID")
                if group_id in groups and row != groups[group_id]:
                    raise ValueError("Study snapshot contains conflicting source records")
                groups[group_id] = row
    return groups


def source_asset(url):
    if not isinstance(url, str):
        raise ValueError("Missing source media URL")
    uri = urljoin(PAGE, url)
    if approved_host(uri) != "zenlishtoeic.vn" or not urlsplit(uri).path.startswith("/wp-content/uploads/"):
        raise ValueError("Media URL differs from the saved source")
    return uri


def parse_candidate(record):
    sub = record.get("sub_questions")
    if not isinstance(sub, list) or not sub or any(not isinstance(q, dict) for q in sub):
        raise ValueError("Missing source questions")
    numbers = []
    for q in sub:
        match = re.match(r"^([1-9][0-9]{0,3})[.):]", plain_text(q.get("title")))
        number = source_integer(q["index"]) if "index" in q else int(match[1]) if match else None
        if number is None:
            raise ValueError("Source question number missing")
        numbers.append(number)
    part = next((i for i, end in enumerate(PART_ENDS, 1) if numbers[0] <= end), 0)
    if not part or numbers[-1] > PART_ENDS[part - 1] or numbers != list(range(numbers[0], numbers[0] + len(sub))):
        raise ValueError("Source numbers are not contiguous within their Part")
    sizes = {1: (1,), 2: (1,), 3: (3,), 4: (3,), 5: (1,), 6: (4,), 7: (2, 3, 4, 5)}
    if len(sub) not in sizes[part] or record.get("is_grouped") is not (part in (3, 4, 6, 7)):
        raise ValueError("Group size or flag disagrees with the Part")
    for name in ("part", "part_number"):
        if name in record and source_integer(record[name]) != part:
            raise ValueError("Source Part disagrees with the question numbers")
    if record.get("type") != ("listening" if part <= 4 else "reading"):
        raise ValueError("Wrong source question type")
    audio = None
    if part <= 4:
        audio = source_asset(record.get("audio_url"))
        span = "-".join(map(str, (numbers[0], numbers[-1]))) if len(sub) > 1 else str(numbers[0])
        if not urlsplit(audio).path.endswith(f"-part-{part}-{span}.mp3"):
            raise ValueError("Audio filename disagrees with the Part or question numbers")
    elif record.get("audio_url"):
        raise ValueError("Reading group points to audio")
    questions = normalize_questions(record, PAGE, part=part, indices=tuple(numbers))
    markup = html.unescape(record.get("content") or "")
    photo_urls = {source_asset(q["image_source_url"]) for q in questions if q["image_source_url"]}
    for element in (markup, *(html.unescape(q.get("title") or "") for q in sub)):
        parser = PageMarkup()
        parser.feed(element)
        photo_urls.update(source_asset(src) for src in parser.images)
    if len(photo_urls) > 1 or (photo_urls and part not in {1, 6, 7}) or (part == 1 and not photo_urls):
        raise ValueError("Missing required image or unsupported image group")
    passage = plain_text(markup) or None
    image = next(iter(photo_urls), None)
    if part in (6, 7) and not (image or passage):
        raise ValueError("Missing Reading passage")
    return part, questions, passage if part in (6, 7) else None, audio, image


def fetch_asset(client, url, media, kind):
    response = client.get(url, limit=MAX_MEDIA, accept="audio/mpeg, application/octet-stream" if kind == "audio"
                          else "image/png, image/jpeg")
    try:
        inspect_access(response)
    except FetchError:
        client.blocked_hosts.add(approved_host(url))
        raise
    if urlsplit(response.url).path != urlsplit(url).path:
        raise ValueError("Redirect did not retain the exact media path")
    info = check_audio(response, url) if kind == "audio" else inspect_media(response.body)
    if kind == "image" and not (info["mime"] in ("image/png", "image/jpeg") and info["mime"] == response.content_type):
        raise ValueError("Image MIME and bytes disagree")
    if kind == "audio" and not 1 <= info["duration_seconds"] <= 360:
        raise ValueError("MP3 duration outside Study bounds")
    asset = package_media(response.body, media, kind)
    return asset, {"url": response.url, **info}


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def check_source_page(client, url, batch):
    try:
        result = client.get(url, limit=MAX_PAGE, accept="text/html, application/json")
        text = result.body.decode("utf-8-sig", errors="strict")
        parser = PageMarkup()
        parser.feed(text)
        if page_restricted(text, parser):
            client.blocked_hosts.add(approved_host(url))
            return {"url": url, "status": "BLOCKED", "reason": "Access interstitial"}
        digest = sha256(result.body).hexdigest()
        (batch / f"{digest}.html").write_bytes(result.body)
        return {"url": result.url, "status": "PAGE_ONLY", "sha256": digest, "bytes": len(result.body)}
    except (FetchError, ValueError) as error:
        return {"url": url, "status": "BLOCKED" if getattr(error, "blocked", False) else "PARTIAL",
                "reason": str(error)}


def acquire(batch=BATCH):
    page_file = SOURCE / "zenlish-p3-q32-34/source_page.html"
    snapshot = page_file.read_bytes()
    version = sha256(snapshot).hexdigest()
    receipt = read_json(page_file.with_name("acquisition.json"))["page"]
    if receipt["url"] != PAGE or receipt["sha256"] != version or receipt["bytes"] != len(snapshot):
        raise ValueError("Source snapshot differs from its acquisition receipt")
    base = read_json(ROOT / "assets/study_pack/pack.json")
    if sum(len(group["items"]) for group in base["practice"]) != 17:
        raise ValueError("Start acquisition from the original 17-item Study pack")
    records = snapshot_groups(snapshot.decode("utf-8-sig"))
    if not records:
        raise ValueError("No Study groups in the cached source")
    batch.mkdir(exist_ok=False)  # one acquisition; replay and review are offline
    media = batch / "media"
    media.mkdir()
    write_json(batch / "base-pack.json", base)
    client = BoundedClient(max_requests=80, max_bytes=100 * 1024**2)
    groups, evidence, omitted = [], [], []
    existing = {group["id"] for group in base["practice"]}
    seen_media = {g[field]["sha256"] for g in base["practice"] for field in ("audio", "image") if g.get(field)}
    attempted = Counter()
    questions_attempted = 0
    stop_network = False
    for source_id, row in records.items():
        group_id = f"zenlish:{source_id}"
        if group_id in existing:
            continue
        try:
            part, questions, passage, audio_url, image_url = parse_candidate(row)
            if attempted[part] >= PART_TARGETS[part - 1]:
                continue
            if sum(attempted.values()) >= MAX_GROUPS or questions_attempted + len(questions) > MAX_QUESTIONS:
                break
            attempted[part] += 1
            questions_attempted += len(questions)
            if stop_network and (audio_url or image_url):
                omitted.append({"id": group_id, "reason": "Batch network stopped"})
                continue
            audio, audio_meta = fetch_asset(client, audio_url, media, "audio") if audio_url else (None, None)
            image, image_meta = fetch_asset(client, image_url, media, "image") if image_url else (None, None)
            hashes = {asset["sha256"] for asset in (audio, image) if asset}
            if hashes & seen_media:
                raise ValueError("Media already belongs to another practice group")
            items = project_items(questions)
            groups.append({"id": group_id, "part": part, "source": PAGE, "version": version, "passage": passage,
                           "audio": audio, "image": image, "audioItems": [i["id"] for i in items] if audio else [],
                           "items": items})
            evidence.append({"id": group_id, "source_version": version, "audio": audio_meta, "image": image_meta,
                             "answers": {q["id"]: q["answer"]["label"] for q in questions}})
            seen_media.update(hashes)
        except (ValueError, OSError) as error:
            omitted.append({"id": group_id, "reason": str(error)})
            if isinstance(error, FetchError) and error.blocked:
                stop_network = True
    sources = []
    for url in SOURCE_PAGES:
        if stop_network:
            source = {"url": url, "status": "NOT_RUN", "reason": "Batch network stopped"}
        else:
            source = check_source_page(client, url, batch)
            stop_network = source["status"] == "BLOCKED"
        sources.append(source)
    write_json(batch / "new-groups.json", groups)
    result = {"source_version": version, "snapshot_groups": len(records),
              "snapshot_source_keys": sum(isinstance(q.get("answer"), str) and q["answer"].strip().upper() in "ABCD"
                                          and len(q["answer"].strip()) == 1
                                          for row in records.values() for q in row["sub_questions"]),
              "attempted_groups": sum(attempted.values()), "attempted_questions": questions_attempted,
              "accepted_groups": len(groups), "accepted_questions": sum(len(group["items"]) for group in groups),
              "requests": client.requests, "bytes": client.downloaded, "http": client.audit,
              "media_and_keys": evidence, "omitted": omitted, "other_sources": sources}
    write_json(batch / "acquisition.json", result)
    return {key: value for key, value in result.items() if key not in {"http", "media_and_keys", "omitted"}}


if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__).parse_args()
    print(json.dumps(acquire(), ensure_ascii=False))
