#!/usr/bin/env python3
"""Validate a source-agnostic Listening manifest and local media without a network."""
import argparse
from hashlib import sha256
import json
import math
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import urlsplit

sys.dont_write_bytecode = True
from listening_media import inspect_media

MAX_MANIFEST = 4 * 1024**2
MAX_BLOB = 12 * 1024**2


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def digest(value):
    return isinstance(value, str) and bool(re.fullmatch(r"[0-9a-f]{64}", value))


def https_url(value):
    if not nonempty(value) or any(ord(char) <= 32 or char == "\\" for char in value):
        return False
    try:
        url = urlsplit(value)
        return bool(url.scheme == "https" and url.hostname and url.username is None and not url.fragment)
    except ValueError:
        return False


def read_json(path, limit=MAX_MANIFEST):
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("Duplicate JSON object key")
            result[key] = value
        return result

    def reject_constant(_):
        raise ValueError("Invalid JSON number")

    with path.open("rb") as stream:
        data = stream.read(limit + 1)
    if len(data) > limit:
        raise ValueError("JSON exceeds offline size limit")
    return json.loads(data.decode("utf-8"), object_pairs_hook=unique_pairs, parse_constant=reject_constant)


def choose_file(root, value):
    if not nonempty(value) or "\\" in value or ":" in value or any(part in ("", ".", "..") for part in value.split("/")):
        raise ValueError("Expected a portable relative file path")
    path = PurePosixPath(value)
    if path.is_absolute():
        raise ValueError("Absolute paths are not accepted")
    candidate = root.joinpath(*path.parts).resolve()
    if not candidate.is_relative_to(root) or not candidate.is_file():
        raise ValueError("Local file missing or outside the manifest directory")
    return candidate


def read_blob(path, maximum=MAX_BLOB):
    with path.open("rb") as stream:
        data = stream.read(maximum + 1)
    if not data or len(data) > maximum:
        raise ValueError("Local file is empty or too large")
    return data


class Validator:
    def __init__(self, root):
        self.root = root.resolve()
        self.errors, self.holds, self.groups = [], [], []
        self.ids = set()
        self.audio_paths, self.audio_hashes = set(), set()

    def error(self, code, path):
        self.errors.append({"code": code, "path": path})

    def hold(self, code, path):
        self.holds.append({"code": code, "path": path})

    def unique(self, namespace, key, path):
        value = (namespace, key)
        if value in self.ids:
            self.error("DUPLICATE_ID", path)
        self.ids.add(value)

    def identifier(self, row, field, namespace, path):
        value = row.get(field)
        if nonempty(value):
            self.unique(namespace, value, path)
        else:
            self.error("MISSING_ID", path)

    def verify_file(self, row, kind, path):
        if not isinstance(row, dict):
            self.error("MISSING_" + kind.upper(), path)
            return
        self.identifier(row, "id", "media", path)
        if not https_url(row.get("source_url")):
            self.error("MISSING_MEDIA_PROVENANCE", path)
        try:
            file = choose_file(self.root, row.get("path"))
            data = read_blob(file)
        except (OSError, ValueError):
            self.error("MISSING_OR_UNSAFE_FILE", path)
            return
        if type(row.get("bytes")) is not int or row["bytes"] != len(data):
            self.error("BYTE_COUNT_MISMATCH", path)
        actual_hash = sha256(data).hexdigest()
        if not digest(row.get("sha256")) or row["sha256"] != actual_hash:
            self.error("CHECKSUM_MISMATCH", path)
        if kind == "audio":
            if file in self.audio_paths or actual_hash in self.audio_hashes:
                self.error("DUPLICATE_AUDIO", path)
            self.audio_paths.add(file)
            self.audio_hashes.add(actual_hash)
        try:
            measured = inspect_media(data)
        except ValueError:
            self.error("CORRUPT_OR_UNSUPPORTED_MEDIA", path)
            return
        if (not measured["mime"].startswith(kind + "/") or measured["mime"] != row.get("mime")
                or measured["format"] != row.get("format")):
            self.error("MEDIA_TYPE_MISMATCH", path)
            return
        if kind == "audio":
            if any(type(row.get(k)) is not int or row[k] != measured[k] for k in ("channels", "sample_rate_hz")):
                self.error("AUDIO_STREAM_METADATA_MISMATCH", path)
            seconds = row.get("duration_seconds")
            if (type(seconds) not in (int, float) or not math.isfinite(seconds)
                    or abs(seconds - measured["duration_seconds"]) > 0.001
                    or row.get("duration_method") != measured["duration_method"]):
                self.error("AUDIO_DURATION_MISMATCH", path)
            if row.get("decode_status") not in ("PASS", "NOT_RUN") or row.get("probe_status") == "FAIL":
                self.error("AUDIO_DECODER_FAILED_OR_UNKNOWN", path)
            elif row["decode_status"] != "PASS" and measured["format"] == "mp3":
                self.hold("COMPRESSED_DECODE_NOT_RUN", path)

    def verify_source(self, value, path):
        if (not isinstance(value, dict) or not nonempty(value.get("site"))
                or not https_url(value.get("page_url")) or not digest(value.get("snapshot_sha256"))
                or not nonempty(value.get("version")) or not nonempty(value.get("retrieved_at_utc"))):
            self.error("MISSING_SOURCE_VERSION_OR_PROVENANCE", path)
            return None
        if value.get("snapshot_path") is not None:
            try:
                data = read_blob(choose_file(self.root, value["snapshot_path"]))
                if sha256(data).hexdigest() != value["snapshot_sha256"]:
                    self.error("SOURCE_SNAPSHOT_HASH_MISMATCH", path)
            except (OSError, ValueError):
                self.error("MISSING_OR_UNSAFE_SOURCE_SNAPSHOT", path)
        return value["site"]

    def verify_question(self, q, path, group, part, site):
        if not isinstance(q, dict):
            self.error("MISSING_OR_INVALID_QUESTION", path)
            return None, None
        self.identifier(q, "id", "question", path)
        source_id = q.get("source_item_id")
        if source_id is not None:
            if not nonempty(source_id):
                self.error("INVALID_SOURCE_ITEM_ID", path)
            elif site is not None:
                self.unique("source-question:" + site, source_id, path)
        if q.get("group_id") != group:
            self.error("WRONG_QUESTION_GROUP", path)
        labels = "ABC" if part == 2 else "ABCD"
        choices = q.get("choices")
        if not isinstance(choices, dict) or set(choices) != set(labels):
            self.error("MISSING_OR_WRONG_CHOICES", path)
        elif q.get("presentation") == "SOURCE_LABELS_ONLY" and part in (1, 2):
            if q.get("prompt") is not None or any(choices[label] != "" for label in labels):
                self.error("INCONSISTENT_LABEL_ONLY_RECORD", path)
            self.hold("SOURCE_TEXT_ABSENT", path)
        elif (q.get("presentation") != "WRITTEN" or not nonempty(q.get("prompt"))
              or not all(nonempty(choices[label]) for label in labels)):
            self.error("MISSING_QUESTION_TEXT", path)
        answer = q.get("answer")
        if not isinstance(answer, dict) or answer.get("status") == "ANSWER_KEY_UNVERIFIED":
            self.hold("ANSWER_KEY_UNVERIFIED", path)
            if isinstance(answer, dict) and answer.get("label") is not None:
                self.error("UNSUPPORTED_ANSWER_LABEL", path)
        elif answer.get("label") not in tuple(labels) or not nonempty(answer.get("evidence")):
            self.error("INVALID_ANSWER_EVIDENCE", path)
        elif answer.get("status") == "SOURCE_EXPLICIT":
            self.hold("ANSWER_REVIEW_REQUIRED", path)
        elif answer.get("status") != "VERIFIED":
            self.error("UNKNOWN_ANSWER_STATUS", path)
        image = q.get("image")
        if part == 1 or q.get("image_required") is True or image is not None:
            self.verify_file(image, "image", path + ".image")
            if isinstance(image, dict) and (image.get("group_id"), image.get("item_id")) != (group, q.get("id")):
                self.error("WRONG_IMAGE_BINDING", path)
        return q.get("id"), q.get("index")

    def verify_group(self, group, index):
        path = f"groups[{index}]"
        start = len(self.errors)
        if not isinstance(group, dict):
            self.error("INVALID_GROUP", path)
            return
        part, group_id = group.get("part"), group.get("id")
        self.identifier(group, "id", "group", path)
        if type(part) is not int or part not in range(1, 5):
            self.error("INVALID_PART", path)
        if type(group.get("sequence")) is not int or group["sequence"] != index + 1:
            self.error("WRONG_GROUP_SEQUENCE", path)
        site = self.verify_source(group.get("source"), path + ".source")
        if not nonempty(group.get("source_group_id")):
            self.error("MISSING_SOURCE_GROUP_ID", path)
        elif site is not None:
            self.unique("source-group:" + site, group["source_group_id"], path)
        retrieval = group.get("retrieval_status")
        if retrieval not in ("FETCHED", "PARTIAL", "BLOCKED", "NOT_RUN"):
            self.error("UNKNOWN_RETRIEVAL_STATUS", path)
        elif retrieval != "FETCHED":
            self.hold("ACQUISITION_INCOMPLETE", path)

        questions = group.get("questions")
        if not isinstance(questions, list) or not questions:
            self.error("MISSING_QUESTIONS", path)
            questions = []
        if part in (1, 2) and len(questions) != 1:
            self.error("WRONG_SINGLE_ITEM_COUNT", path)
        pairs = [self.verify_question(q, f"{path}.questions[{i}]", group_id, part, site)
                 for i, q in enumerate(questions)]
        ids, indices = [q[0] for q in pairs], [q[1] for q in pairs]
        expected = group.get("expected_indices")
        if (not indices or any(type(n) is not int or n < 1 for n in indices)
                or any(b != a + 1 for a, b in zip(indices, indices[1:])) or indices != expected
                or not isinstance(expected, list) or any(type(n) is not int for n in expected)):
            self.error("QUESTION_ORDER_OR_COUNT_MISMATCH", path)

        audio = group.get("audio")
        self.verify_file(audio, "audio", path + ".audio")
        if isinstance(audio, dict):
            binding = group.get("audio_binding")
            if (audio.get("group_id") != group_id or audio.get("item_ids") != ids
                    or not isinstance(binding, dict) or not https_url(binding.get("url"))
                    or not nonempty(binding.get("id")) or binding["id"] != audio.get("id")
                    or binding["url"] != audio.get("requested_url")):
                self.error("WRONG_AUDIO_BINDING", path)
        for field, reviewed, allowed in (
            ("qa", "APPROVED", ("NOT_RUN", "PENDING", "APPROVED", "REJECTED")),
            ("rights", "VERIFIED_FOR_SCOPE", ("PO_DECLARED_NOT_INSPECTED", "UNVERIFIED",
                                            "VERIFIED_FOR_SCOPE", "NOT_ALLOWED")),
        ):
            record = group.get(field)
            state = record.get("status") if isinstance(record, dict) else None
            if state not in allowed:
                self.error(field.upper() + "_STATUS_MISSING_OR_INVALID", path)
            elif state != reviewed or not nonempty(record.get("evidence")):
                self.hold(field.upper() + "_REVIEW_REQUIRED", path)
        qa = group.get("qa")
        recognized_retrieval = retrieval if retrieval in ("FETCHED", "PARTIAL", "BLOCKED", "NOT_RUN") else None
        qa_state = qa.get("status") if isinstance(qa, dict) else None
        self.groups.append({"group_id": group_id if isinstance(group_id, str) else None,
                            "retrieval": recognized_retrieval,
                            "mapping": "MAPPED" if len(self.errors) == start else "UNMAPPED",
                            "declared_qa": qa_state if qa_state in ("NOT_RUN", "PENDING", "APPROVED", "REJECTED") else None})

    def validate(self, manifest):
        if not isinstance(manifest, dict) or type(manifest.get("schema_version")) is not int or manifest["schema_version"] != 1:
            self.error("UNSUPPORTED_SCHEMA", "$")
        else:
            groups = manifest.get("groups")
            if not isinstance(groups, list) or not 1 <= len(groups) <= 4:
                self.error("INVALID_GROUP_COUNT", "groups")
            elif sum(len(group["questions"]) for group in groups
                     if isinstance(group, dict) and isinstance(group.get("questions"), list)) > 15:
                self.error("QUESTION_LIMIT_EXCEEDED", "groups")
            else:
                for index, group in enumerate(groups):
                    self.verify_group(group, index)
        # The CLI reports what the local declarations and bytes support.
        # Readiness continues to require separately authorized review.
        return {"status": "INVALID" if self.errors else "HOLD" if self.holds else "REVIEW_REQUIRED",
                "eligible_for_app": False, "groups": self.groups, "errors": self.errors, "holds": self.holds}


def main(argv=None):
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("manifest", type=Path)
    args = cli.parse_args(argv)
    try:
        path = args.manifest.resolve()
        report = Validator(path.parent).validate(read_json(path))
    except (OSError, ValueError, RecursionError, OverflowError):
        report = {"status": "INVALID", "eligible_for_app": False, "groups": [],
                  "errors": [{"code": "UNREADABLE_OR_INVALID_JSON", "path": "$"}], "holds": []}
    print(json.dumps(report, indent=2, ensure_ascii=True))
    return {"INVALID": 1, "HOLD": 2, "REVIEW_REQUIRED": 0}[report["status"]]


if __name__ == "__main__":
    sys.exit(main())
