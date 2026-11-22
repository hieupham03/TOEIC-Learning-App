"""Lab projection tests use generated records and MPEG frame headers only."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from test_listening_manifest import fixture
from test_zenlish_crawler import frames
from listening_media import inspect_media
from prepare_local_part3_preview import prepare


class LocalPart3PreviewTests(unittest.TestCase):
    def setUp(self):
        directory = TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.document = fixture(self.root)
        self.group = self.document["groups"][2]
        self.group["id"] = "zenlish:41021"
        self.group["qa"] = {"status": "NOT_RUN"}
        for item in self.group["questions"]:
            item["group_id"] = self.group["id"]
            item["id"] = f"{self.group['id']}:{item['index']}"
        self.audio = frames()
        self.path = self.root / "generated.mp3"
        self.path.write_bytes(self.audio)
        self.group["audio"].update(inspect_media(self.audio), path=self.path.name,
                                   group_id=self.group["id"],
                                   item_ids=[item["id"] for item in self.group["questions"]])

    def test_lab_payload_keeps_order_and_never_contains_answer_keys(self):
        metadata, audio = prepare(self.document, self.root)
        preview = json.loads(metadata)
        self.assertEqual(audio, self.audio)
        self.assertEqual([item["number"] for item in preview["items"]], [32, 33, 34])
        self.assertEqual([item["id"] for item in preview["items"]], preview["audio"]["itemIds"])
        self.assertTrue(all(set(item) == {"id", "number", "prompt", "choices"} for item in preview["items"]))
        self.assertNotIn(b"synthetic-only answer reference", metadata)

    def test_reordered_audio_binding_fails(self):
        self.group["audio"]["item_ids"].reverse()
        with self.assertRaisesRegex(ValueError, "WRONG_AUDIO_BINDING"):
            prepare(self.document, self.root)

    def test_missing_audio_fails(self):
        self.path.unlink()
        with self.assertRaisesRegex(ValueError, "Listening manifest failed"):
            prepare(self.document, self.root)

    def test_rejected_candidate_fails(self):
        self.group["qa"]["status"] = "REJECTED"
        with self.assertRaisesRegex(ValueError, "Unexpected Part 3"):
            prepare(self.document, self.root)
