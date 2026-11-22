#!/usr/bin/env python3
"""Prepare the one unscored Part 3 group for the isolated Android lab build."""
from hashlib import sha256
import json
from pathlib import Path
from tempfile import NamedTemporaryFile

from listening_manifest import Validator, choose_file, read_blob, read_json

TOOLING = Path(__file__).resolve().parents[1] / ".tooling"
GROUP_ID = "zenlish:41021"
NUMBERS = [32, 33, 34]
MAX_AUDIO = 2 * 1024**2


def prepare(manifest, source):
    result = Validator(source).validate(manifest)
    if result["errors"]:
        errors = ", ".join(entry["code"] for entry in result["errors"])
        raise ValueError("Listening manifest failed structural checks: " + errors)
    groups = [group for group in manifest["groups"] if group["id"] == GROUP_ID]
    if len(groups) != 1:
        raise ValueError("Expected the single Part 3 lab group")
    group = groups[0]
    audio = group["audio"]
    items = group["questions"]
    if (group["part"] != 3 or group["retrieval_status"] != "FETCHED"
            or group["qa"]["status"] == "REJECTED"
            or [item["index"] for item in items] != NUMBERS
            or [item["id"] for item in items] != [f"{GROUP_ID}:{number}" for number in NUMBERS]
            or audio["format"] != "mp3" or audio["mime"] != "audio/mpeg"):
        raise ValueError("Unexpected Part 3 group, question sequence or audio format")
    payload = read_blob(choose_file(source.resolve(), audio["path"]), MAX_AUDIO)
    if (len(payload), sha256(payload).hexdigest()) != (audio["bytes"], audio["sha256"]):
        raise ValueError("Part 3 audio size or checksum changed")
    preview = {
        "groupId": GROUP_ID,
        "audio": {"groupId": audio["group_id"], "itemIds": audio["item_ids"],
                  "bytes": audio["bytes"], "sha256": audio["sha256"]},
        "items": [{"id": item["id"], "number": item["index"], "prompt": item["prompt"],
                   "choices": [item["choices"][label] for label in "ABCD"]} for item in items],
    }
    content = json.dumps(preview, ensure_ascii=False).encode("utf-8")
    if len(content) > 16 * 1024:
        raise ValueError("Part 3 lab metadata is too large")
    return content, payload


def write_asset(path, content):
    with NamedTemporaryFile(dir=path.parent, delete=False) as staged:
        temporary = Path(staged.name)
        try:
            staged.write(content)
            staged.close()
            temporary.replace(path)
        finally:
            temporary.unlink(missing_ok=True)


def main():
    source = TOOLING / "listening-overnight"
    target = TOOLING / "fasttrack-handoff/part3-assets/listening_preview"
    try:
        metadata, audio = prepare(read_json(source / "normalized_manifest.json"), source)
        target.mkdir(parents=True, exist_ok=True)
        write_asset(target / "part3.mp3", audio)
        write_asset(target / "part3.json", metadata)
    except (OSError, ValueError) as error:
        print(f"BLOCKED: {error}")
        return 1
    print(f"Prepared unscored Part 3 group {GROUP_ID}. MP3 SHA-256 {sha256(audio).hexdigest()}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
