#!/usr/bin/env python3
"""Acquire only the approved public Zenlish group (Part 3 Q32–34)."""
import argparse
from datetime import datetime, timezone
from hashlib import sha256
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import urljoin, urlsplit

sys.dont_write_bytecode = True
from listening_http import BoundedClient, FetchError, MAX_BYTES, MAX_MEDIA, MAX_REQUESTS, Response, approved_host
from listening_media import inspect_media, probe_audio

PAGE = "https://zenlishtoeic.vn/stm-quizzes/test-1-2022/"
AUDIO = "https://zenlishtoeic.vn/wp-content/uploads/2023/04/zenlish-test-01-part-3-32-34.mp3"
GROUP_ID = 41021
INDICES = (32, 33, 34)
ROOT = Path(__file__).resolve().parents[1] / ".tooling/listening-overnight"
PARSER_VERSION = "zenlish-p3/3"
MAX_PAGE = 8 * 1024**2


class PageMarkup(HTMLParser):
    def __init__(self, anchor="41021"):
        super().__init__()
        self.anchor = anchor
        self.documents, self.visible = [], []
        self.script = self.title = False
        self.title_text = ""
        self.has_password = False
        self.images = []

    def handle_starttag(self, tag, attrs):
        self.script |= tag == "script"
        self.title |= tag == "title"
        self.has_password |= tag == "input" and (dict(attrs).get("type") or "").lower() == "password"
        if tag == "img" and dict(attrs).get("src"):
            self.images.append(dict(attrs)["src"])
        self.documents.extend(value for key, value in attrs if key.startswith("data-") and value and self.anchor in value)
        if tag in {"br", "p", "div", "li"}:
            self.visible.append(" ")

    def handle_endtag(self, tag):
        if tag == "script":
            self.script = False
        if tag == "title":
            self.title = False

    def handle_data(self, value):
        if self.title:
            self.title_text += value
        if self.script:
            if self.anchor in value:
                self.documents.append(value)
        else:
            self.visible.append(value)


def plain_text(value):
    if not isinstance(value, str):
        return ""
    parser = PageMarkup()
    parser.feed(value)
    parser.close()
    return " ".join("".join(parser.visible).split())


def page_restricted(text, markup):
    return bool(
        re.search(r"(?i)(just a moment|attention required|access denied|verify (that )?you are human|"
                  r"^\s*(?:login|sign in|đăng nhập)\b)", markup.title_text)
        or re.search(r'(?i)\b(?:cf-chl-[\w-]+|challenge-platform/h/[gb]/orchestrate)\b', text)
        or (markup.has_password and re.search(r"(?i)(login|sign in|đăng nhập)", markup.title_text))
    )


def source_integer(value):
    if type(value) is int and value > 0:
        return value
    if isinstance(value, str) and re.fullmatch(r"[1-9][0-9]{0,11}", value):
        return int(value)
    return None


def json_objects_matching(source, marker):
    # Locate a JSON property without assuming that it is the first member.
    decoder = json.JSONDecoder()
    matches = list(marker.finditer(source))
    if len(matches) > 64:
        raise ValueError("Too many candidate group markers")
    if not matches:
        return
    markers = {match.start() for match in matches}
    stack = []
    visited = set()
    for token in re.finditer(r'"(?:[^"\\]|\\.)*"|[{}\[\]]', source, flags=re.DOTALL):
        value = token[0]
        if value in ("{", "["):
            stack.append((value, token.start()))
        elif value in ("}", "]"):
            if stack and stack[-1][0] == ("{" if value == "}" else "["):
                stack.pop()
            else:
                stack.clear()
        if token.start() not in markers:
            continue
        if not stack or stack[-1][0] != "{":
            continue
        position = stack[-1][1]
        if position in visited:
            continue
        visited.add(position)
        try:
            obj, _ = decoder.raw_decode(source, position)
        except (ValueError, RecursionError):
            continue
        if isinstance(obj, dict):
            yield obj


def embedded_documents(text, anchor, key):
    markup = PageMarkup(anchor)
    markup.feed(text)
    markup.close()
    if page_restricted(text, markup):
        raise FetchError("Page presents a login, CAPTCHA or anti-automation restriction", blocked=True)
    documents = markup.documents.copy()
    if text.lstrip().startswith(("{", "[")):
        documents.append(text)
    if not documents and anchor in text:
        documents.append(html.unescape(text))
    for document in documents:
        versions = [document]
        if "&quot;" in document:
            versions.append(html.unescape(document))
        # Decode JSON.parse("...") or an escaped JSON data string as a JSON
        # string. Do not rewrite quote escapes inside question/choice values.
        escaped_key = r'\"' + key + r'\"'
        if escaped_key in document:
            for string in re.finditer(r'"(?:[^"\\]|\\.)*"', document, flags=re.DOTALL):
                if escaped_key in string[0] and anchor in string[0]:
                    try:
                        versions.append(json.loads(string[0]))
                    except ValueError:
                        pass
        yield from versions


def extract_group(text, page_url=PAGE):
    groups = []
    marker = re.compile(r'"question_id"\s*:\s*(?:41021\b|"41021")')
    for source in embedded_documents(text, "41021", "question_id"):
        for group in json_objects_matching(source, marker):
            if (source_integer(group.get("question_id")) == GROUP_ID
                    and (group.get("is_grouped") is True or "sub_questions" in group) and group not in groups):
                groups.append(group)
    if len(groups) != 1:
        raise ValueError("Expected one distinct embedded group 41021; page structure absent or ambiguous")
    group = groups[0]
    if group.get("is_grouped") is not True:
        raise ValueError("Group is not explicitly grouped")
    for key in ("part", "part_number"):
        if key in group and source_integer(group[key]) != 3:
            raise ValueError("Source declares a different Part")
    if not isinstance(group.get("audio_url"), str) or urljoin(page_url, group["audio_url"]) != AUDIO:
        raise ValueError("Group audio link missing or does not match the approved clip")
    return group


def normalize_questions(group, page_url=PAGE, *, part=3, indices=INDICES):
    group_id = source_integer(group.get("question_id"))
    if group_id is None:
        raise ValueError("Group ID missing")
    labels = "ABC" if part == 2 else "ABCD"
    questions = group.get("sub_questions")
    if not isinstance(questions, list) or any(not isinstance(q, dict) for q in questions):
        raise ValueError("Question records missing or malformed")
    numbers = []
    for q in questions:
        title_number = re.match(r"^([1-9][0-9]{0,3})[.):]\s*", plain_text(q.get("title")))
        index = source_integer(q["index"]) if "index" in q else int(title_number[1]) if title_number else None
        if title_number and index != int(title_number[1]):
            raise ValueError("Question index contradicts visible source number")
        numbers.append(index)
    if tuple(numbers) != indices:
        raise ValueError("Unexpected question numbers or source order")
    normalized, seen = [], set()
    for index, q in zip(indices, questions):
        for key in ("group_id", "parent_id"):
            if key in q and source_integer(q[key]) != group_id:
                raise ValueError("Question linked to a different parent group")
        provided = next((q[key] for key in ("sub_question_id", "id", "question_id") if key in q), None)
        source_id = source_integer(provided)
        if provided is not None and source_id is None:
            raise ValueError("Malformed source question ID")
        if source_id == group_id and "id" not in q and "sub_question_id" not in q:
            source_id = None  # Some pages repeat the parent ID on its children.
        if source_id is not None and source_id in seen:
            raise ValueError("Duplicate source question ID")
        if source_id is not None:
            seen.add(source_id)
        choices = q.get("choices")
        if "choices" not in q and isinstance(q.get("answer"), list):
            choices = q["answer"]  # In the observed page variant this is an option list.
        if isinstance(choices, dict) and set(choices) == set(labels):
            choices = [{"choice": label, "choice_answer": choices[label]} for label in labels]
        if (not isinstance(choices, list) or any(not isinstance(c, dict) for c in choices)
                or [c.get("choice") for c in choices] != list(labels)):
            raise ValueError("Missing, duplicate or unordered question choices")
        values = [plain_text(c.get("choice_answer")) for c in choices]
        prompt = plain_text(q.get("title"))
        labels_only = (part in {1, 2} and re.fullmatch(r"[1-9][0-9]{0,3}[.):]", prompt)
                       and not any(values))
        if not labels_only and (not prompt or not all(values)):
            raise ValueError("Question or choice text missing")
        answer = q.get("answer")
        # An explicit A–D key in the item field is attributable to the page,
        # while correctness and rights still require separate review.
        explicit = answer.strip().upper() if isinstance(answer, str) else None
        key = explicit if explicit in tuple(labels) else None
        image_url = None
        if q.get("image_url"):
            if not isinstance(q["image_url"], str):
                raise ValueError("Malformed image association")
            image_url = urljoin(page_url, q["image_url"])
        normalized.append({"id": f"zenlish:{group_id}:{index}", "source_item_id": source_id,
                           "group_id": str(group_id), "index": index, "prompt": None if labels_only else prompt,
                           "presentation": "SOURCE_LABELS_ONLY" if labels_only else "WRITTEN",
                           "choices": dict(zip(labels, values)), "image_source_url": image_url,
                           "answer": {"label": key, "status": "SOURCE_EXPLICIT" if key else "ANSWER_KEY_UNVERIFIED",
                                      "evidence_url": page_url if key else None}})
    return normalized


def check_audio(response, expected_url=None):
    if response.content_type not in {"audio/mpeg", "audio/mp3", "application/octet-stream"}:
        raise ValueError("Audio response MIME is not an accepted MP3 type")
    if expected_url and urlsplit(response.url).path.rsplit("/", 1)[-1] != urlsplit(expected_url).path.rsplit("/", 1)[-1]:
        raise ValueError("Redirected media no longer matches the group's named clip")
    metadata = inspect_media(response.body)
    if metadata["format"] != "mp3":
        raise ValueError("Expected MP3 framing")
    return metadata


def self_test():
    fixture = {"audio_url": AUDIO, "is_grouped": True, "question_id": GROUP_ID, "sub_questions": [
        {"index": index, "question_id": GROUP_ID, "title": "Synthetic prompt",
         "choices": {label: f"Synthetic choice {label}" for label in "ABCD"}}
        for index in INDICES]}
    page = "<script>window.sample = " + json.dumps(fixture) + ";</script>"
    assert len(normalize_questions(extract_group(page))) == 3
    print("PASS: one synthetic exact-group parser self-test; no live request")


def run(output, client, previous=None):
    report = {"status": "BLOCKED", "part": 3, "source": "zenlishtoeic.vn", "group_id": str(GROUP_ID),
              "source_page": PAGE, "expected_indices": list(INDICES), "groups": 0, "questions": 0,
              "rights_status": "PO_DECLARED_NOT_INSPECTED", "qa_status": "NOT_RUN",
              "retrieved_at_utc": datetime.now(timezone.utc).isoformat(), "parser_version": PARSER_VERSION,
              "errors": []}
    try:
        if previous is None:
            page = client.get(PAGE, limit=MAX_PAGE, accept="text/html, application/json")
            (output / "source_page.html").write_bytes(page.body)
        else:
            source = previous["page"]
            page = Response(source["url"], source["response_status"], source["mime"],
                            (output / "source_page.html").read_bytes())
            if len(page.body) > MAX_PAGE or len(page.body) != source["bytes"] or sha256(page.body).hexdigest() != source["sha256"]:
                raise ValueError("Saved page bytes do not match the prior receipt")
            report["reused_saved_page"] = True
            report["retrieved_at_utc"] = previous["retrieved_at_utc"]
        report["status"] = "PARTIAL"
        report["page"] = {"url": page.url, "bytes": len(page.body), "sha256": sha256(page.body).hexdigest(),
                          "response_status": page.status, "mime": page.content_type}
        if page.content_type not in {"text/html", "application/xhtml+xml", "application/json"}:
            raise ValueError("Unexpected HTML/JSON page MIME")
        group = extract_group(page.body.decode("utf-8-sig", errors="strict"), page.url)
        questions = normalize_questions(group, page.url)
        report.update(groups=1, questions=len(questions), question_indices=[q["index"] for q in questions],
                      source_question_ids=[q["source_item_id"] for q in questions],
                      explicit_answer_count=sum(q["answer"]["status"] == "SOURCE_EXPLICIT" for q in questions))
        (output / "questions.json").write_text(json.dumps(questions, ensure_ascii=False, indent=2), encoding="utf-8")
        audio = client.get(AUDIO, limit=MAX_MEDIA, accept="audio/mpeg, application/octet-stream")
        if audio.content_type == "text/html":
            text = audio.body.decode("utf-8", errors="replace")
            markup = PageMarkup()
            markup.feed(text)
            if page_restricted(text, markup):
                raise FetchError("Audio endpoint presents an access restriction", blocked=True)
        media = check_audio(audio, AUDIO)
        audio_file = output / "audio.mp3"
        audio_file.write_bytes(audio.body)
        media.update(probe_audio(audio_file), url=audio.url, response_status=audio.status,
                     declared_mime=audio.content_type, path=audio_file.name)
        report["audio"] = media
        if "FAIL" in {media["decode_status"], media["probe_status"]}:
            report["errors"].append("Local codec tool reported failure")
        elif any(q.get("image_source_url") for q in questions):
            report["errors"].append("Page declares an image association outside this exact audio-only target")
        else:
            report["status"] = "FETCHED"
    except FetchError as error:
        report["errors"].append(str(error))
        report["source_stopped"] = error.blocked
        if error.blocked and not report["groups"]:
            report["status"] = "BLOCKED"
    except (ValueError, RecursionError) as error:
        report["errors"].append(type(error).__name__ if isinstance(error, UnicodeError) else str(error))
    report.update(http_requests=client.requests, downloaded_bytes=client.downloaded, request_audit=client.audit)
    (output / "acquisition.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def continue_from_receipt(output, previous):
    """Reparse the saved page once while carrying the original batch ledger."""
    audit = previous.get("request_audit", [])
    if (previous.get("status") != "PARTIAL" or previous.get("source_stopped")
            or previous.get("audio") or previous.get("reused_saved_page")
            or not audit or len(audit) != previous.get("http_requests")
            or len(audit) >= MAX_REQUESTS or previous.get("downloaded_bytes", MAX_BYTES) >= MAX_BYTES
            or not isinstance(previous.get("page"), dict)
            or previous["page"].get("response_status") != 200
            or approved_host(previous["page"].get("url", "")) != "zenlishtoeic.vn"
            or any(entry.get("url") == AUDIO for entry in audit)):
        raise ValueError("Receipt is not eligible for one local-page continuation")
    client = BoundedClient()
    client.requests = len(audit)
    client.downloaded = previous["downloaded_bytes"]
    client.audit = audit.copy()
    client.last_start["zenlishtoeic.vn"] = client.now()
    with (output / "acquisition_initial.json").open("x", encoding="utf-8") as marker:
        json.dump(previous, marker, ensure_ascii=False, indent=2)
    return run(output, client, previous)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "zenlish-p3-q32-34")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--resume-local-page", action="store_true",
                        help="Reparse a saved partial page and continue within its existing HTTP budget")
    args = parser.parse_args(argv)
    if args.self_test:
        self_test()
        return 0
    out = args.output.resolve()
    if ROOT.resolve() != ROOT or not out.is_relative_to(ROOT) or out == ROOT:
        parser.error("--output must be a child of android-app/.tooling/listening-overnight")
    saved = out / "acquisition.json"
    if saved.is_file():
        report = json.loads(saved.read_text(encoding="utf-8"))
        if args.resume_local_page:
            try:
                report = continue_from_receipt(out, report)
            except (ValueError, FileExistsError) as error:
                parser.error(str(error))
        else:
            print(f"Previous receipt reused ({report['status']}); no requests sent")
    else:
        if args.resume_local_page:
            parser.error("No prior receipt to resume")
        if out.exists() and any(out.iterdir()):
            parser.error("Output already contains evidence without a completed receipt")
        out.mkdir(parents=True, exist_ok=True)
        (out / "batch.started").touch(exist_ok=False)
        report = run(out, BoundedClient())
    print(f"{report['status']}: {report['groups']} group(s), {report['questions']} question(s), "
          f"{report['http_requests']} HTTP attempts, {report['downloaded_bytes']} body bytes")
    return 0 if report["status"] == "FETCHED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
