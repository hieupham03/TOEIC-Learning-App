"""Stage verified publisher question/key pairs for the private Study review pipeline."""
from argparse import ArgumentParser
from hashlib import sha256
from pathlib import Path
import re
from shutil import copy2

from activate_study_content import item_binding
from crawl_one_zenlish_part3_group import plain_text
from extend_study_content import ROOT02, save_json
from listening_manifest import read_blob, read_json

WORKSPACE = ROOT02.parent / "content-04"
FAUST_PAPER = "https://www.faustacademy.com/pruefungsmaterial/toeic-lr-reading-01"
ENGLISHCLUB_PAPER = "https://www.englishclub.com/esl-exams/ets-toeic-practice-5.php"
ENGLISHCLUB_MEMO = "https://www.englishclub.com/esl-exams/ets-toeic-practice-7.php"


def faust_revision(paper_url, key_url, source):
    parent = source.rstrip("/") + "/revisions/"
    match = re.fullmatch(re.escape(parent) + r"([0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12})/candidate\.pdf", paper_url)
    if match is None or key_url != parent + match[1] + "/teacher.pdf":
        raise ValueError("Question and key PDFs do not share the publisher revision")
    return match[1]


def split_choices(block, marker):
    matches = list(marker.finditer(block))
    if [match[1] for match in matches] != list("ABCD"):
        raise ValueError("Choices must appear exactly once in A–D order")
    prompt = " ".join(block[:matches[0].start()].split())
    choices = [" ".join(block[match.end():matches[index + 1].start() if index < 3 else len(block)].split())
               for index, match in enumerate(matches)]
    if not prompt or any(not choice for choice in choices):
        raise ValueError("Question stem or option is empty")
    return prompt, choices


def faust_part5(paper_pages):
    eligible = False
    lines = []
    for number, page in enumerate(paper_pages, 1):
        page_lines = [raw.strip() for raw in page.splitlines()]
        if page_lines[:2] == ["Faust", str(number)]:
            page_lines = page_lines[2:]
        for line in page_lines:
            if line == "Part 5" and re.search(r"(?m)^101\.\s", page):
                eligible = True
            elif eligible and line == "Part 6":
                break
            elif eligible and line and not re.fullmatch(r"(?i)(?:Faust Academy\b.*|faustacademy\.com/\S+|"
                                                        r"go on to the next page[.!]?)", line):
                lines.append(line)
        else:
            continue
        break
    text = "\n".join(lines)
    numbers = list(re.finditer(r"(?m)^(10[1-9]|1[12][0-9]|130)\.\s+", text))
    if [int(marker[1]) for marker in numbers] != list(range(101, 131)):
        raise ValueError("Faust Part 5 numbering is incomplete or out of order")
    return {
        int(marker[1]): split_choices(text[marker.end():numbers[index + 1].start() if index + 1 < len(numbers) else len(text)],
                                      re.compile(r"\(([ABCD])\)"))
        for index, marker in enumerate(numbers)
    }


def faust_public_keys(key_pages, questions):
    result = {}
    for page, text in enumerate(key_pages, 1):
        for match in re.finditer(r"(?m)^[ \t]*([0-9]{1,3})[ \t]*:[ \t]*([ABCD])[ \t]*$", text):
            number = int(match[1])
            if number not in questions or number in result:
                raise ValueError("Unexpected or duplicate publisher key")
            result[number] = (match[2], f"PDF page {page}, question {number}")
    if not result:
        raise ValueError("PDF contains no attributable keys")
    return result


def englishclub_public_p5(page):
    markers = list(re.finditer(r"<h2\b[^>]*>\s*Example\s+([0-9]+):\s*</h2>", page, re.I))
    if [int(marker[1]) for marker in markers] != [1, 2, 3, 4]:
        raise ValueError("Unexpected EnglishClub Part 5 examples")
    result = {}
    for index, marker in enumerate(markers):
        block = page[marker.end():markers[index + 1].start() if index + 1 < len(markers) else len(page)]
        question = " ".join(plain_text(bits) for bits in re.findall(r'<p class="clr-blue">(.+?)</p>', block, re.S))
        prompt, choices = split_choices(question, re.compile(r"\b([ABCD])\)"))
        keys = re.findall(r"The correct answer is\s+([ABCD])\b", plain_text(block), re.I)
        if len(keys) != 1:
            raise ValueError("Publisher example has missing or ambiguous key")
        number = int(marker[1])
        result[number] = ((prompt, choices), (keys[0].upper(), f"Example {number}, correct answer paragraph"))
    return result


def englishclub_memo(page):
    section = re.search(r"<h2>Example 1: Memo</h2>(.+?)<h2>Example 2:", page, re.S)
    if section is None:
        raise ValueError("EnglishClub memo example not found")
    passage = re.search(r'<div class="clr-blue"[^>]*>(.+?)</div>', section[1], re.S)
    if passage is None or not plain_text(passage[1]):
        raise ValueError("Missing memo passage")
    items = []
    keys = {}
    start = passage.end()
    headings = list(re.finditer(r'<p class="clr-blue">([0-9]+)\.\s', section[1][start:]))
    if [int(marker[1]) for marker in headings] != [1, 2]:
        raise ValueError("Memo question order does not match the source")
    for index, marker in enumerate(headings):
        end = start + headings[index + 1].start() if index + 1 < len(headings) else len(section[1])
        block = section[1][start + marker.end():end]
        prompt = block.partition("</p>")[0]
        options = re.findall(r'<p class="clr-blue">(.+?)</p>', block, re.S)
        if len(options) != 1:
            raise ValueError("Memo question has missing or ambiguous options")
        text, choices = split_choices(plain_text(prompt + " " + options[0]), re.compile(r"\b([ABCD])\)"))
        letters = re.findall(r"The correct answer is\s+([ABCD])\b", plain_text(block), re.I)
        if len(letters) != 1:
            raise ValueError("Memo key is missing or ambiguous")
        number = int(marker[1])
        items.append({"id": f"englishclub-p7:memo:{number}", "number": number, "prompt": text, "choices": choices})
        keys[number] = letters[0].upper()
    return plain_text(passage[1]), items, keys


def groups_with_keys(issuer, source, version, key_url, key_digest, questions, keys):
    groups, rows = [], []
    for number, (label, locator) in keys.items():
        prompt, choices = questions[number]
        item = {"id": f"{issuer}:{number}:q", "number": number, "prompt": prompt, "choices": choices}
        group = {"id": f"{issuer}:{number}", "part": 5, "source": source, "version": version, "items": [item]}
        groups.append(group)
        rows.append({**item_binding(group, item), "label": label, "evidenceUrl": key_url,
                     "evidenceSha256": key_digest, "locator": locator})
    return groups, rows


def pdf_pages(body):
    import pymupdf

    if not body.startswith(b"%PDF-"):
        raise ValueError("Publisher response is not PDF")
    with pymupdf.open(stream=body, filetype="pdf") as document:
        if document.needs_pass:
            raise ValueError("Encrypted PDF")
        # Faust draws its watermark separately. Coordinate sorting mixes it into stems and options.
        return [page.get_text(sort=False) for page in document]


def publisher_file(workspace, ledger, name):
    receipt = ledger[name]
    body = read_blob(workspace / name)
    digest = sha256(body).hexdigest()
    if digest != receipt["sha256"] or len(body) != receipt["bytes"]:
        raise ValueError(f"Saved publisher file differs from its receipt: {name}")
    return body, receipt["url"], digest


def prepare(workspace=WORKSPACE):
    ledger = read_json(workspace / "publisher-files.json")
    raw, paper_url, raw_sha = publisher_file(workspace, ledger, "faust-r01-candidate.pdf")
    teacher, key_url, key_sha = publisher_file(workspace, ledger, "faust-r01-teacher.pdf")
    revision = faust_revision(paper_url, key_url, FAUST_PAPER)
    paper_pages, key_pages = pdf_pages(raw), pdf_pages(teacher)
    displayed_path = FAUST_PAPER.removeprefix("https://www.")
    if displayed_path not in paper_pages[0] or displayed_path not in key_pages[0]:
        raise ValueError("Publication printed inside candidate/key PDFs differs")
    questions = faust_part5(paper_pages)
    keys = faust_public_keys(key_pages, questions)
    groups, rows = groups_with_keys("faust-r01", FAUST_PAPER, raw_sha, key_url, key_sha, questions, keys)
    englishclub, club_url, club_sha = publisher_file(workspace, ledger, "englishclub-p5.html")
    memo, memo_url, memo_sha = publisher_file(workspace, ledger, "englishclub-p7.html")
    if club_url != ENGLISHCLUB_PAPER or memo_url != ENGLISHCLUB_MEMO:
        raise ValueError("Unexpected EnglishClub publication URL")
    examples = englishclub_public_p5(englishclub.decode("utf-8-sig"))
    club_groups, club_rows = groups_with_keys(
        "englishclub-p5", ENGLISHCLUB_PAPER, club_sha, ENGLISHCLUB_PAPER, club_sha,
        {n: pair[0] for n, pair in examples.items()}, {n: pair[1] for n, pair in examples.items()},
    )
    passage, items, memo_keys = englishclub_memo(memo.decode("utf-8-sig"))
    memo_group = {"id": "englishclub-p7:memo", "part": 7, "source": memo_url, "version": memo_sha,
                  "items": items, "passage": passage, "passageItems": [item["id"] for item in items]}
    memo_rows = [{**item_binding(memo_group, item), "label": memo_keys[item["number"]], "evidenceUrl": memo_url,
                  "evidenceSha256": memo_sha, "locator": f"Example 1 Memo, answer {item['number']}"} for item in items]
    owner = workspace / "owner"
    sources = owner / "sources"
    evidence = workspace / "source-evidence"
    for directory in (sources, evidence):
        directory.mkdir(parents=True, exist_ok=True)
    write_once = ((sources, raw_sha, raw), (sources, club_sha, englishclub), (sources, memo_sha, memo),
                  (evidence, key_sha, teacher), (evidence, club_sha, englishclub), (evidence, memo_sha, memo))
    for directory, digest, body in write_once:
        (directory / f"{digest}.bin").write_bytes(body)
    save_json(owner / "bundle.json", {"schema": 1, "practice": groups + club_groups + [memo_group], "inventories": []})
    save_json(owner / "source-keys.json", rows + club_rows + memo_rows)
    copy2(ROOT02 / "new-groups.json", workspace / "new-groups.json")
    media = workspace / "media"
    media.mkdir(exist_ok=True)
    for file in (ROOT02 / "media").iterdir():
        if file.is_file() and not (media / file.name).exists():
            copy2(file, media / file.name)
    result = {"faust": {"revision": revision, "paper_url": paper_url, "key_url": key_url,
                        "paper_hash": raw_sha, "key_hash": key_sha, "part5_items": len(questions),
                        "public_keys": len(keys), "paper_pages": len(paper_pages), "key_pages": len(key_pages)},
              "englishclub": {"part5_hash": club_sha, "part7_hash": memo_sha, "public_keys": len(club_rows) + len(memo_rows)}}
    save_json(workspace / "publisher-import.json", result)
    return result


if __name__ == "__main__":
    import json

    ArgumentParser(description=__doc__).parse_args()
    print(json.dumps(prepare(), ensure_ascii=False))
