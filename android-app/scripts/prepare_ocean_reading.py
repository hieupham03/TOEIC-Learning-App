"""Stage 100 questions from a pinned MIT-licensed Reading bank for local review."""
from argparse import ArgumentParser
from collections import Counter
from hashlib import sha256
import json
import os
from pathlib import Path
import re
from shutil import copy2, copytree
import subprocess

from activate_study_content import item_binding, optional_rows
from extend_study_content import ROOT02, save_json
from listening_manifest import read_json
from review_study_content import assemble

REVISION = "a940bb8b479ef4d06af468015d757041c3d2e457"
REPOSITORY = "https://github.com/kdeppaei/toeic-question-ocean"
EDITION_URL = f"{REPOSITORY}/tree/{REVISION}"
SOURCE_HASHES = {
    "question-bank-v29.js": "ea0b0a91a94c0b313167e3fa7a150668141f47cfaaf4927e2aa299b03a67bdbc",
    "question-bank-v30.js": "8901965ab305e9f1a8f8cc6b6223f31a2d850af1d8d5afcc2e84a44a87893daa",
    "question-bank-v45.js": "310bf29d62dab1faca77146239939cedf43d72de1a94922935b8b99476660c3e",
    "question-bank-v46.js": "e3adac78721b2489c57093078dcef5ed0e44df258e0f4a4ec1f5aa250fed0636",
    "question-bank-v50.js": "045b40030342196ba8441ab3ffd9279c89fa8dffe9e85cf645a2eaf000ca559b",
}
LICENSE_HASH = "9d58a6ceeaab47fae1a77aa5ce2f96393c6c117e4e82ea6c28e878d408f128de"
BASELINE = ROOT02.parent / "content-06/voa-review"
WORKSPACE = ROOT02.parent / "content-07"


def read_pinned(folder, name, digest):
    body = (folder / f"ocean-{name}").read_bytes()
    if sha256(body).hexdigest() != digest:
        raise ValueError(f"Source SHA-256 differs for {name}")
    return body


def pinned_rows(files, acorn):
    parser = Path(__file__).with_name("extract_ocean_literals.cjs")
    collection = json.dumps({name: body.decode("utf-8") for name, body in files.items()}).encode()
    output = subprocess.run(["node", str(parser)], input=collection,
                            env={**os.environ, "NODE_PATH": str(acorn)}, capture_output=True, check=True, timeout=30)
    return json.loads(output.stdout)


def section(rows, version, name):
    entries = rows[f"question-bank-v{version}.js"]
    return [(version, entry) for entry in entries if entry["section"] == name]


def project(rows, revision):
    selections = {
        5: section(rows, 30, "grammarItems")[:30],
        6: section(rows, 45, "part6Groups") + section(rows, 50, "part6Groups")[:2],
        7: (
            [pair for pair in section(rows, 45, "readingGroups") if pair[1]["value"]["groupId"] in {"P7-R91", "P7-R92"}]
            + section(rows, 46, "readingGroups") + section(rows, 50, "readingGroups")
            + [pair for pair in section(rows, 29, "inline") if pair[1]["value"].get("groupId") in {"P7-R54", "P7-R55"}]
        ),
    }
    groups, keys, distribution = [], [], Counter()
    number = 0
    for part, selected in selections.items():
        for version, entry in selected:
            raw = entry["value"]
            code = raw["id"] if part == 5 else raw["groupId"]
            questions = [raw] if part == 5 else raw.get("questions", raw.get("items"))
            if not re.fullmatch(rf"P{part}-[A-Z0-9]+", code):
                raise ValueError("Source group ID does not match the Part")
            group = {"id": f"ocean:{code}", "part": part, "source": EDITION_URL, "version": revision, "items": []}
            if part >= 6:
                group["passage"] = raw["passage"]
            file = f"question-bank-v{version}.js"
            for index, question in enumerate(questions, 1):
                number += 1
                label, options = question["answer"], question["choices"]
                if type(label) is not int or not 0 <= label <= 3 or len(options) != 4:
                    raise ValueError(f"Invalid ordered options or key in {code}, item {index}")
                item_code = question.get("id", f"{code}-Q{index}")
                item = {"id": f"ocean:{item_code}", "number": number, "prompt": question["prompt"], "choices": options}
                group["items"].append(item)
                keys.append({**item_binding(group, item), "label": "ABCD"[label],
                             "evidenceUrl": f"{REPOSITORY}/blob/{REVISION}/{file}",
                             "evidenceSha256": SOURCE_HASHES[file],
                             "locator": f"line {entry['questionLines'][index - 1]}, {item_code}"})
                distribution[part] += 1
            if part >= 6:
                group["passageItems"] = [item["id"] for item in group["items"]]
            groups.append(group)
    if distribution != {5: 30, 6: 16, 7: 54} or len({key["itemId"] for key in keys}) != len(keys):
        raise ValueError("The selected batch must be 100 unique questions with intact groups")
    return groups, keys


def stage(source, acorn, workspace=WORKSPACE, baseline=BASELINE):
    license_text = read_pinned(source, "LICENSE", LICENSE_HASH)
    files = {name: read_pinned(source, name, digest) for name, digest in SOURCE_HASHES.items()}
    receipt = {"edition": REVISION, "publisher": "TOEIC Question Ocean", "license": LICENSE_HASH, "files": SOURCE_HASHES}
    receipt_bytes = json.dumps(receipt, sort_keys=True).encode()
    revision = sha256(receipt_bytes).hexdigest()
    groups, keys = project(pinned_rows(files, acorn), revision)
    workspace.mkdir(exist_ok=True)
    for name in ("owner", "media", "source-evidence"):
        if not (workspace / name).exists():
            copytree(baseline / name, workspace / name)
    for name in ("new-groups.json", "review-decisions.json"):
        if not (workspace / name).exists():
            copy2(baseline / name, workspace / name)
    owner = workspace / "owner"
    (owner / "sources" / f"{revision}.bin").write_bytes(receipt_bytes)
    for name, body in files.items():
        (workspace / "source-evidence" / f"{SOURCE_HASHES[name]}.bin").write_bytes(body)
    bundle = read_json(owner / "bundle.json")
    bundle["practice"] = [group for group in bundle["practice"] if group["source"] != EDITION_URL] + groups
    previous = optional_rows(owner / "source-keys.json")
    save_json(owner / "bundle.json", bundle)
    save_json(owner / "source-keys.json", [row for row in previous if row["source"] != EDITION_URL] + keys)
    report = assemble(workspace)
    notice = workspace / "assets/TOEIC_QUESTION_OCEAN_LICENSE.txt"
    notice.write_bytes(license_text)
    save_json(workspace / "ocean-source-receipt.json", {**receipt, "editionSha256": revision,
              "candidateItems": 100, "sourceLabels": Counter(row["label"] for row in keys)})
    return report


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True, help="Local source-discovery folder with pinned ocean-* files")
    parser.add_argument("--acorn", type=Path, required=True, help="Local Node module directory containing Acorn")
    arguments = parser.parse_args()
    print(json.dumps(stage(arguments.source.resolve(), arguments.acorn.resolve()), ensure_ascii=False))
