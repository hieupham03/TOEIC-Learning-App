"""Synthetic fixtures only. The tests do not import the acquisition client."""
from copy import deepcopy
from hashlib import sha256
from io import BytesIO, StringIO
import json
from pathlib import Path
import struct
import sys
from tempfile import TemporaryDirectory
import unittest
from contextlib import redirect_stdout
import wave
import zlib

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import listening_manifest as manifest
from listening_media import inspect_media


def wav(seed):
    out = BytesIO()
    with wave.open(out, "wb") as audio:
        audio.setparams((1, 2, 8000, 0, "NONE", "not compressed"))
        audio.writeframes(struct.pack("<800h", *[seed if i % 2 else -seed for i in range(800)]))
    return out.getvalue()


def png():
    def chunk(tag, payload):
        return struct.pack(">I", len(payload)) + tag + payload + struct.pack(">I", zlib.crc32(tag + payload))
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", 1, 1, 8, 0, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(b"\x00\x80")) + chunk(b"IEND", b""))


def fixture(root):
    groups = []
    (root / "synthetic_source.json").write_text("{}", encoding="utf-8")
    for part, indices in enumerate(((1,), (7,), (32, 33, 34), (71, 72, 73)), 1):
        group_id = f"synthetic-{part}"
        asset = f"synthetic-{part}.wav"
        payload = wav(part)
        (root / asset).write_bytes(payload)
        media_url = "https://synthetic.invalid/" + asset
        questions = []
        for number in indices:
            questions.append({
                "id": f"{group_id}:{number}", "group_id": group_id, "source_item_id": str(number), "index": number,
                "presentation": "WRITTEN", "prompt": "Generated prompt",
                "choices": {label: f"Generated option {label}" for label in ("ABC" if part == 2 else "ABCD")},
                "answer": {"label": "A", "status": "VERIFIED", "evidence": "synthetic-only answer reference"},
            })
        if part == 1:
            photo = png()
            (root / "synthetic.png").write_bytes(photo)
            questions[0]["image"] = {"id": "image-1", "group_id": group_id, "item_id": questions[0]["id"],
                                     "path": "synthetic.png", "source_url": "https://synthetic.invalid/image.png",
                                     **inspect_media(photo)}
        groups.append({
            "id": group_id, "source_group_id": f"source-{part}", "part": part, "sequence": part,
            "source": {"site": "synthetic.invalid", "page_url": "https://synthetic.invalid/group",
                       "version": "synthetic-v1", "retrieved_at_utc": "2026-01-01T00:00:00Z",
                       "snapshot_sha256": sha256(b"{}").hexdigest(), "snapshot_path": "synthetic_source.json"},
            "retrieval_status": "FETCHED", "expected_indices": list(indices), "questions": questions,
            "audio_binding": {"id": asset, "url": media_url},
            "audio": {"id": asset, "group_id": group_id, "item_ids": [q["id"] for q in questions],
                      "source_url": media_url, "requested_url": media_url, "path": asset,
                      **inspect_media(payload), "decode_status": "NOT_RUN"},
            "qa": {"status": "APPROVED", "evidence": "synthetic-only QA declaration"},
            "rights": {"status": "VERIFIED_FOR_SCOPE", "evidence": "synthetic-only rights declaration"},
        })
    return {"schema_version": 1, "groups": groups}


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.document = fixture(self.root)
        self.groups = self.document["groups"]

    def result(self, document=None):
        return manifest.Validator(self.root).validate(self.document if document is None else document)

    def assert_error(self, code, document=None):
        result = self.result(document)
        self.assertEqual(result["status"], "INVALID")
        self.assertFalse(result["eligible_for_app"])
        self.assertIn(code, [item["code"] for item in result["errors"]])

    def test_structural_pass_never_exports_or_makes_app_eligible(self):
        result = self.result()
        self.assertEqual(result["status"], "REVIEW_REQUIRED")
        self.assertEqual([group["mapping"] for group in result["groups"]], ["MAPPED"] * 4)
        self.assertFalse(result["eligible_for_app"])

    def test_full_cli_reports_distinct_exit_codes(self):
        path = self.root / "synthetic_manifest.json"
        for state, code in (("APPROVED", 0), ("NOT_RUN", 2), ("unexpected", 1)):
            self.groups[0]["qa"]["status"] = state
            path.write_text(json.dumps(self.document), encoding="utf-8")
            with redirect_stdout(StringIO()) as stdout:
                self.assertEqual(manifest.main([str(path)]), code)
                self.assertFalse(json.loads(stdout.getvalue())["eligible_for_app"])

    def test_no_audio_and_missing_required_image(self):
        self.groups[0]["audio"] = None
        self.groups[0]["questions"][0].pop("image")
        self.assert_error("MISSING_AUDIO")
        self.assert_error("MISSING_IMAGE")

    def test_missing_question_wrong_choices_or_ordinals(self):
        self.groups[2]["questions"].reverse()
        self.assert_error("QUESTION_ORDER_OR_COUNT_MISMATCH")
        self.groups[1]["questions"][0]["choices"].pop("B")
        self.assert_error("MISSING_OR_WRONG_CHOICES")
        self.groups[3]["questions"] = []
        self.assert_error("MISSING_QUESTIONS")

    def test_wrong_group_sequence_and_group_reference(self):
        self.groups[0]["sequence"] = 2
        self.groups[2]["questions"][0]["group_id"] = "wrong"
        self.assert_error("WRONG_GROUP_SEQUENCE")
        self.assert_error("WRONG_QUESTION_GROUP")

    def test_wrong_audio_source_or_order_mapping(self):
        self.groups[2]["audio"]["item_ids"].reverse()
        self.assert_error("WRONG_AUDIO_BINDING")
        self.groups[2]["audio"]["item_ids"].reverse()
        self.groups[2]["audio"]["requested_url"] = "https://synthetic.invalid/unrelated.wav"
        self.assert_error("WRONG_AUDIO_BINDING")

    def test_wrong_image_binding(self):
        self.groups[0]["questions"][0]["image"]["item_id"] = "unrelated-item"
        self.assert_error("WRONG_IMAGE_BINDING")

    def test_duplicate_ids_and_duplicate_audio_bytes(self):
        self.groups[1]["id"] = self.groups[0]["id"]
        self.groups[1]["questions"][0]["id"] = self.groups[0]["questions"][0]["id"]
        (self.root / "synthetic-2.wav").write_bytes(wav(1))
        self.groups[1]["audio"].update(inspect_media(wav(1)))
        self.assert_error("DUPLICATE_ID")
        self.assert_error("DUPLICATE_AUDIO")

    def test_detects_corruption_even_with_updated_checksum(self):
        bad = wav(2)[:-4]
        (self.root / "synthetic-2.wav").write_bytes(bad)
        self.groups[1]["audio"].update(bytes=len(bad), sha256=sha256(bad).hexdigest())
        self.assert_error("CORRUPT_OR_UNSUPPORTED_MEDIA")
        image = bytearray(png())
        image[30] ^= 0x01
        (self.root / "synthetic.png").write_bytes(image)
        self.assert_error("CORRUPT_OR_UNSUPPORTED_MEDIA")

    def test_jpeg_marker_fragments_without_valid_segments_are_rejected(self):
        with self.assertRaises(ValueError):
            inspect_media(b"\xff\xd8\xff\xda\xff\xd9")

    def test_checksum_bytes_and_duration_mismatch(self):
        row = self.groups[0]["audio"]
        row.update(sha256="0" * 64, bytes=12, duration_seconds=20.0)
        for code in ("CHECKSUM_MISMATCH", "BYTE_COUNT_MISMATCH", "AUDIO_DURATION_MISMATCH"):
            self.assert_error(code)

    def test_paths_fail_closed(self):
        for path in ("missing.wav", "../outside.wav", "C:/outside.wav", "\\outside\\audio.wav"):
            self.groups[0]["audio"]["path"] = path
            self.assert_error("MISSING_OR_UNSAFE_FILE")

    def test_source_snapshot_is_checked(self):
        (self.root / "synthetic_source.json").write_text('{"changed":true}', encoding="utf-8")
        self.assert_error("SOURCE_SNAPSHOT_HASH_MISMATCH")

    def test_review_gaps_separate_from_structural_errors(self):
        group = self.groups[0]
        group["qa"] = {"status": "NOT_RUN", "evidence": None}
        group["rights"] = {"status": "PO_DECLARED_NOT_INSPECTED", "evidence": None}
        group["questions"][0].pop("answer")
        result = self.result()
        self.assertEqual(result["status"], "HOLD")
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["groups"][0]["mapping"], "MAPPED")
        self.assertEqual({item["code"] for item in result["holds"]},
                         {"ANSWER_KEY_UNVERIFIED", "QA_REVIEW_REQUIRED", "RIGHTS_REVIEW_REQUIRED"})

    def test_labels_only_is_hold_but_absent_written_text_is_invalid(self):
        question = self.groups[1]["questions"][0]
        question.update(presentation="SOURCE_LABELS_ONLY", prompt=None, choices=dict.fromkeys("ABC", ""))
        self.assertEqual(self.result()["status"], "HOLD")
        question["presentation"] = "WRITTEN"
        self.assert_error("MISSING_QUESTION_TEXT")

    def test_unknown_shapes_raise_no_exception(self):
        for value in (None, 1, ["synthetic"], {"schema_version": True, "groups": []},
                      {"schema_version": 1, "groups": [None]}):
            with self.subTest(value=value):
                self.assertEqual(manifest.Validator(self.root).validate(value)["status"], "INVALID")
        broken = deepcopy(self.document)
        broken["groups"][0].update(part={}, questions=[[], {}], rights=[], audio="missing")
        self.assertEqual(self.result(broken)["status"], "INVALID")

    def test_json_duplicate_keys_and_nan_rejected(self):
        path = self.root / "broken.json"
        for text in ('{"schema_version":1,"schema_version":2}', '{"test":NaN}'):
            path.write_text(text, encoding="utf-8")
            with self.assertRaises(ValueError):
                manifest.read_json(path)


if __name__ == "__main__":
    unittest.main()
