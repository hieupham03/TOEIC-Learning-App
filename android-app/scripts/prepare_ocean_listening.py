"""Build private Listening practice from exact author assets and local synthesized English speech."""
import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import random
import re
from shutil import copy2, copytree
import subprocess
from tempfile import TemporaryDirectory
import wave

from activate_study_content import item_binding, optional_rows
from extend_study_content import ROOT02, save_json
from listening_manifest import read_json
from prepare_ocean_reading import EDITION_URL, LICENSE_HASH, REPOSITORY, REVISION, pinned_rows
from prepare_study_pack import package_media
from review_study_content import assemble

FILES = {
    "question-bank.js": "aefb6b1dbfb2ba235dc79a558cf0b5b3ed6682127acb3f868290048de7aaa32f",
    "question-bank-v31.js": "1c37829024d646f62d3d4fcaafb9cc39125abbc2fa2fa1da2c91523c1be4f78b",
    "question-bank-v32.js": "b3ac073d3c7c07273cb26c2122b8e1b655fe9f303147d2474bd755c5497b1e4c",
    "question-bank-v33.js": "ca8aaa2f6cac20f73575c00ea3527b42f14128f26553c14a215421561f7e95e2",
    "question-bank-v34.js": "7e229073afcf52e7a10cff074f7466d76270b0cea767ac3f7e24ae7b9a7c14d1",
}
ATTRIBUTION = "assets/part1/ATTRIBUTION.md"
ATTRIBUTION_HASH = "1abb0e25f7f9450c5472b5f4450c93c22feeed477705ccd4aa5e19240dddc805"
BASE = "question-bank.js"
TARGET = ROOT02.parent / "content-08"
PRIOR = ROOT02.parent / "content-07"
SAMPLE_RATE = 44100
SCOPE = "SOURCE_KEY_PRACTICE"


def pinned_file(root, name, digest):
    body = (root / name).read_bytes()
    if sha256(body).hexdigest() != digest:
        raise ValueError(f"Pinned source mismatch: {name}")
    return body


def flat_bank(body):
    assignment = body.decode("utf-8").strip()
    prefix = "window.BUILTIN_BANK = "
    if not assignment.startswith(prefix) or not assignment.endswith(";"):
        raise ValueError("Unexpected root question-bank assignment")
    return json.loads(assignment[len(prefix):-1])


def select_groups(base, pictures):
    picture_ids = {f"P1-{n:03d}" for n in (1, 5, 6, 9, 10, 11, 12, 13)}
    response_ids = {f"P2-{n:03d}" for n in range(1, 23) if n not in {18, 20}}
    part1 = [(q["id"], 1, [(file, q)]) for file, q in pictures if q["id"] in picture_ids]
    part2 = [(q["id"], 2, [(BASE, q)]) for q in base if q["part"] == "2" and q["id"] in response_ids]
    groups = defaultdict(list)
    for q in base:
        if q["part"] in {"3", "4"}:
            groups[(int(q["part"]), q["groupId"])].append((BASE, q))
    chosen = part1 + part2
    for (part, group), items in groups.items():
        selected = range(2, 10) if part == 3 else range(1, 9)
        if group in {f"P{part}-G{n:02d}" for n in selected}:
            if len(items) != 3 or len({item["audioText"] for _, item in items}) != 1:
                raise ValueError(f"Passage is not an exact 3-question source group: {group}")
            if any(re.search(r"\b(?:look at the|shown in the|the graphic)\b", item["prompt"], re.I) for _, item in items):
                raise ValueError(f"Source group may require separate graphics: {group}")
            chosen.append((group, part, items))
    chosen.sort(key=lambda group: (group[1], group[0]))
    if Counter(part for _, part, _ in chosen) != {1: 8, 2: 20, 3: 8, 4: 8}:
        raise ValueError("Listening batch does not match the selected complete groups")
    if len({q["id"] for _, _, rows in chosen for _, q in rows}) != 76:
        raise ValueError("Duplicate or missing source ID")
    return chosen


def ordered_question(row, number, spoken_slot=None):
    choices = row["choices"]
    correct = row["answer"]
    size = 3 if row["id"].startswith("P2-") else 4
    if (len(choices) != size or len(set(choices)) != size or not all(choices)
            or type(correct) is not int or correct not in range(size)):
        raise ValueError(f"Invalid original key or choices: {row['id']}")
    order = list(range(size))
    if spoken_slot is not None:
        order.remove(correct)
        order.insert(spoken_slot, correct)
    question = {"id": f"ocean:{row['id']}", "number": number,
                "prompt": row.get("audioText", "") if size == 3 else row.get("prompt", ""),
                "choices": [choices[index] for index in order]}
    return question, order.index(correct), order


def speech_turns(part, source, questions):
    if part <= 2:
        lead = source.get("audioText", "")
        if part == 2 and not lead:
            raise ValueError("Part 2 lacks the spoken question")
        options = [(("M" if i % 2 == 0 else "W"), f"Choice {'ABCD'[i]}. {choice}")
                   for i, choice in enumerate(questions[0]["choices"])]
        return ([("W", lead)] if part == 2 else []) + options
    passage = source["audioText"].strip()
    transcript = re.split(r"(?:^|\s)([MW]):\s*", passage)
    if part == 3:
        if transcript[0] or len(transcript) < 5:
            raise ValueError("Dialogue lacks distinguishable author speaker turns")
        turns = list(zip(transcript[1::2], transcript[2::2]))
    else:
        turns = [("W", passage)]
    return turns + [("M", f"Question {question['number']}. {question['prompt']}") for question in questions]


def encode_audio(encoder_class, wav_dir, clip_id, turn_count):
    encoder = encoder_class()
    encoder.set_bit_rate(80)
    encoder.set_in_sample_rate(SAMPLE_RATE)
    encoder.set_channels(1)
    encoder.set_quality(2)
    with_silence = bytearray(bytes(SAMPLE_RATE // 5))
    for index in range(turn_count):
        with wave.open(str(wav_dir / f"{clip_id}-{index}.wav"), "rb") as data:
            if (data.getframerate(), data.getsampwidth(), data.getnchannels()) != (SAMPLE_RATE, 2, 1):
                raise ValueError(f"Unexpected speech output format: {clip_id}")
            pcm = data.readframes(data.getnframes())
        if len(pcm) < SAMPLE_RATE // 2 or not any(pcm):
            raise ValueError(f"Empty speech segment: {clip_id}/{index}")
        with_silence.extend(pcm)
        with_silence.extend(bytes(SAMPLE_RATE))
    return bytes(encoder.encode(bytes(with_silence)) + encoder.flush())


def stage(source, acorn, workspace, baseline, encoder):
    files = {name: pinned_file(source, name, digest) for name, digest in FILES.items()}
    license_text = pinned_file(source, "LICENSE", LICENSE_HASH)
    attribution = pinned_file(source, ATTRIBUTION, ATTRIBUTION_HASH)
    attribution_text = attribution.decode("utf-8")
    pictures = [(file, row["value"]) for file, rows in pinned_rows(
        {file: body for file, body in files.items() if file != BASE}, acorn).items()
        for row in rows if row["section"] == "items"]
    chosen = select_groups(flat_bank(files[BASE]), pictures)
    version_body = json.dumps({"upstream": REVISION, "files": FILES, "attribution": ATTRIBUTION_HASH,
                               "presentation": "listening-08-sapi-1"}, sort_keys=True).encode()
    version = sha256(version_body).hexdigest()

    for name in ("owner", "media", "base-media", "source-evidence"):
        copytree(baseline / name, workspace / name, dirs_exist_ok=True)
    for name in ("new-groups.json", "review-decisions.json"):
        copy2(baseline / name, workspace / name)
    owner = workspace / "owner"
    (owner / "sources" / f"{version}.bin").write_bytes(version_body)
    for name, body in files.items():
        (workspace / "source-evidence" / f"{FILES[name]}.bin").write_bytes(body)

    receipt = read_json(source / "source-receipt.json")
    clips, keyed_groups, distribution = [], [], {part: Counter() for part in range(1, 5)}
    number = Counter()
    # Balance the spoken labels without rotating in a predictable cycle or shuffling after recording.
    slots = {1: list(range(4)) * 2, 2: list(range(3)) * 7}
    for part, order in slots.items():
        random.Random(f"{version}:{part}").shuffle(order)
    for group_id, part, rows in chosen:
        group = {"id": f"ocean:{group_id}", "source": EDITION_URL, "version": version, "part": part, "items": []}
        proof_rows = []
        for file, original in rows:
            spoken_slot = slots[part][number[part]] if part in slots else None
            number[part] += 1
            question, choice, order = ordered_question(original, sum(number.values()), spoken_slot)
            if question["choices"][choice] != original["choices"][original["answer"]]:
                raise ValueError(f"Spoken option does not map to publisher key: {question['id']}")
            group["items"].append(question)
            proof_rows.append((file, original, choice, order))
            distribution[part]["ABCD"[choice]] += 1
        if part == 1:
            image = rows[0][1]["image"]
            if not re.fullmatch(r"assets/part1/[a-z0-9-]+-ai-v\d+\.jpg", image) or f"`{Path(image).name}`" not in attribution_text:
                raise ValueError(f"Image is outside the attributed generated set: {group_id}")
            picture = pinned_file(source, image, receipt["files"][image]["sha256"])
            group["image"] = package_media(picture, owner / "media", "image")
            group["imageItems"] = [group["items"][0]["id"]]
        turns = speech_turns(part, rows[0][1], group["items"])
        clips.append({"id": group_id, "turns": turns})
        keyed_groups.append((group, proof_rows))

    bundle = read_json(owner / "bundle.json")
    keys = optional_rows(owner / "source-keys.json")
    decisions = optional_rows(workspace / "review-decisions.json")
    audit = []
    with TemporaryDirectory(prefix="ocean-listening-", dir=workspace) as work:
        output = Path(work)
        plan = output / "speech-plan.json"
        save_json(plan, clips)
        subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File",
                        str(Path(__file__).with_name("render_study_speech.ps1")), "-Plan", str(plan), "-Output", work],
                       check=True, timeout=360)
        for (group, proof_rows), clip in zip(keyed_groups, clips, strict=True):
            body = encode_audio(encoder, output, clip["id"], len(clip["turns"]))
            group["audio"] = package_media(body, owner / "media", "audio")
            group["audioItems"] = [item["id"] for item in group["items"]]
            bundle["practice"].append(group)
            for item, (file, row, choice, order) in zip(group["items"], proof_rows, strict=True):
                proof = {**item_binding(group, item), "label": "ABCD"[choice],
                         "evidenceUrl": f"{REPOSITORY}/blob/{REVISION}/{file}",
                         "evidenceSha256": FILES[file], "locator": f"Author question {row['id']}"}
                keys.append(proof)
                decisions.append({**proof, "status": "APPROVED", "reviewedAt": "2026-11-25",
                                  "reviewer": "Study engineering – publisher key and media mapping",
                                  "reviewScope": SCOPE})
                audit.append({"itemId": item["id"], "sourceIndex": row["answer"], "presentation": order,
                              "packIndex": choice, "audioSha256": group["audio"]["sha256"]})
    save_json(owner / "bundle.json", bundle)
    save_json(owner / "source-keys.json", keys)
    save_json(workspace / "review-decisions.json", decisions)
    save_json(workspace / "speech-plan.json", clips)
    save_json(workspace / "ocean-listening-audit.json", audit)
    result = assemble(workspace)
    if result["published_forms"] or sum(part["reviewed"] for part in result["counts"].values()) != 190:
        raise ValueError("Unexpected graded count or mock availability after import")
    assets = workspace / "assets"
    (assets / "TOEIC_QUESTION_OCEAN_LICENSE.txt").write_bytes(license_text)
    (assets / "TOEIC_QUESTION_OCEAN_PHOTO_PROVENANCE.txt").write_bytes(attribution)
    copytree(assets, workspace / "release-assets", dirs_exist_ok=True)
    print(json.dumps({"source_version": version, "new_questions": dict(number), "key_positions": distribution,
                      "activation": result}, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--acorn", type=Path, required=True)
    args = parser.parse_args()
    from lameenc import Encoder
    stage(args.source.resolve(), args.acorn.resolve(), TARGET.resolve(), PRIOR.resolve(), Encoder)
