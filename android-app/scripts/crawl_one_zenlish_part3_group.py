#!/usr/bin/env python3
"""Fetch ONE public Zenlish Part 3 group (questions 32–34 + its MP3).

No login, session cookies, CAPTCHA bypass, or bulk crawling.
Outputs stay in .tooling/, which is ignored by the Android repo.
Run from android-app/:
    python scripts/crawl_one_zenlish_part3_group.py --self-test
    python scripts/crawl_one_zenlish_part3_group.py --output .tooling/one-listening-sample
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import sys
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

PAGE = "https://zenlishtoeic.vn/stm-quizzes/test-1-2022/"
AUDIO = "https://zenlishtoeic.vn/wp-content/uploads/2023/04/zenlish-test-01-part-3-32-34.mp3"
GROUP_ID = 41021
EXPECTED_INDICES = (32, 33, 34)
MAX_HTML_BYTES = 8 * 1024 * 1024
MAX_AUDIO_BYTES = 12 * 1024 * 1024
HEADERS = {
    "User-Agent": "TOEIC-Learning-App/one-sample research (manual PO request; one public page)",
    "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
}


def read_bounded(url: str, limit: int) -> tuple[bytes, str]:
    if url not in (PAGE, AUDIO):
        raise ValueError("Unexpected endpoint")
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=20) as resp:
        final = resp.geturl()
        if urlsplit(final).hostname != "zenlishtoeic.vn" or urlsplit(final).scheme != "https":
            raise ValueError("Refusing cross-site/insecure redirect")
        data = resp.read(limit + 1)
        if len(data) > limit:
            raise ValueError(f"Response exceeds {limit} byte limit")
        return data, resp.headers.get("Content-Type", "")


def find_group(raw_html: str) -> dict | None:
    """Find the exact group JSON embedded in the public page scripts."""
    normalized = html.unescape(raw_html).replace("\\/", "/")
    candidates = [normalized]
    if r'\"question_id\"' in normalized:
        candidates.append(normalized.replace(r'\"', '"'))
    decoder = json.JSONDecoder()
    for source in candidates:
        for match in re.finditer(r'\{\s*"question_id"\s*:\s*41021\b', source):
            try:
                found, _ = decoder.raw_decode(source[match.start():])
            except (ValueError, json.JSONDecodeError):
                continue
            if (isinstance(found, dict)
                and found.get("question_id") == GROUP_ID
                and found.get("audio_url") == AUDIO
                and found.get("is_grouped") is True):
                return found
    return None


def summarize_group(group: dict) -> list[dict]:
    questions = group.get("sub_questions")
    if not isinstance(questions, list) or len(questions) != 3:
        raise ValueError("Source did not supply exactly 3 questions")
    indices = tuple(q.get("index") for q in questions)
    if indices != EXPECTED_INDICES:
        raise ValueError(f"Unexpected question order: {indices}")
    clean = []
    for q in questions:
        choices = q.get("choices")
        if not isinstance(choices, list) or [c.get("choice") for c in choices] != ["A", "B", "C", "D"]:
            raise ValueError(f"Unexpected choices for {q.get('index')}")
        clean.append({
            "index": q["index"],
            "question_id": q.get("question_id"),
            "prompt": q.get("title"),
            "choices": [{"label": c["choice"], "text": c.get("choice_answer") or ""} for c in choices],
            "answer_from_page": q.get("answer") or None,
        })
    return clean


def looks_like_mp3(data: bytes) -> bool:
    return len(data) > 1024 and (
        data.startswith(b"ID3") or (data[0] == 0xFF and data[1] & 0xE0 == 0xE0)
    )


def self_test() -> None:
    fixture = {
        "question_id": GROUP_ID,
        "sub_questions": [
            {"title": f"{i}. Placeholder?", "index": i, "question_id": GROUP_ID,
             "answer": "", "choices": [{"choice": v, "choice_answer": f"Option {v}"} for v in "ABCD"]}
            for i in EXPECTED_INDICES
        ],
        "title": "TEST 1 2022. Part 3.32-34",
        "is_grouped": True,
        "audio_url": AUDIO,
    }
    doc = '<script>window.quiz={"41021":' + json.dumps(fixture) + '};</script>'
    got = find_group(doc)
    assert got and got["question_id"] == GROUP_ID
    assert len(summarize_group(got)) == 3
    assert find_group(doc.replace("2023/04", "2022/04")) is None
    assert looks_like_mp3(b"ID3" + b"X" * 1024)
    assert not looks_like_mp3(b"<html>" + b"X" * 1024)
    print("PASS: local parser, group ID, question order, audio URL, MP3 signature")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(".tooling/one-listening-sample"))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    out = args.output
    out.mkdir(parents=True, exist_ok=True)
    status = {
        "sample_id": "ZENLISH-2022-P3-Q32-34",
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_name": "Zenlish TEST 1 – 2022",
        "source_page": PAGE,
        "audio_url": AUDIO,
        "group_id": GROUP_ID,
        "part": 3,
        "question_numbers": list(EXPECTED_INDICES),
        "question_count": None,
        "audio_downloaded": False,
        "source_rights": "PO rights self-attested; asset-specific conditions not independently inspected",
        "content_qa": "NOT_RUN",
        "answer_key": "NOT_VERIFIED",
        "publish_status": "HOLD",
        "errors": [],
    }
    try:
        page_bytes, content_type = read_bounded(PAGE, MAX_HTML_BYTES)
        status["page_bytes"] = len(page_bytes)
        status["page_content_type"] = content_type
        status["page_sha256"] = hashlib.sha256(page_bytes).hexdigest()
        (out / "source_page.html").write_bytes(page_bytes)
        group = find_group(page_bytes.decode("utf-8", errors="replace"))
        if group is None:
            status["errors"].append(
                "Could not extract group 41021 from public HTML; question JSON may load dynamically"
            )
        else:
            questions = summarize_group(group)
            status["question_count"] = len(questions)
            status["group_title"] = group.get("title")
            (out / "questions_32_34.json").write_text(
                json.dumps(questions, ensure_ascii=False, indent=2), encoding="utf-8"
            )
    except (OSError, ValueError, HTTPError, URLError) as e:
        status["errors"].append("HTML: " + str(e)[:320])
    try:
        audio, content_type = read_bounded(AUDIO, MAX_AUDIO_BYTES)
        if not looks_like_mp3(audio):
            raise ValueError("Unexpected response; source not recognized as MP3")
        (out / "audio_32_34.mp3").write_bytes(audio)
        status["audio_downloaded"] = True
        status["audio_bytes"] = len(audio)
        status["audio_sha256"] = hashlib.sha256(audio).hexdigest()
        status["audio_content_type"] = content_type
    except (OSError, ValueError, HTTPError, URLError) as e:
        status["errors"].append("MP3: " + str(e)[:320])
    (out / "manifest.json").write_text(
        json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(status, ensure_ascii=False, indent=2))
    if status["audio_downloaded"] and status["question_count"] == 3:
        print("ONE SAMPLE FETCHED: group and MP3; still NOT_QA_READY")
        return 0
    print("PARTIAL/BLOCKED: see manifest.json; no full crawl PASS.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
