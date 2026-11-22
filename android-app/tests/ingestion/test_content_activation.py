"""Synthetic evidence and packaging cases. No source packets or live I/O."""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from test_listening_manifest import png
from acquire_study_content import parse_candidate
from activate_study_content import activate_groups, item_binding, verify_media
from prepare_study_pack import package_media

URL = "https://zenlishtoeic.vn/synthetic-fixture/"
VERSION = "a" * 64


def group():
    return {"id": "synthetic-group", "source": URL, "version": VERSION, "part": 5, "items": [
        {"id": "one", "number": 101, "prompt": "Choose an option", "choices": ["One", "Two", "Three", "Four"]},
    ]}


class ContentActivationTests(unittest.TestCase):
    def evidence(self, root, row):
        raw = b"Synthetic answer sheet for item one, choice C."
        digest = sha256(raw).hexdigest()
        (root / f"{digest}.bin").write_bytes(raw)
        candidate = {**item_binding(row, row["items"][0]), "label": "C", "evidenceSha256": digest,
                     "evidenceUrl": URL, "locator": "Sheet row one"}
        return candidate, {**candidate, "status": "APPROVED", "reviewer": "synthetic-reviewer"}

    def test_source_key_waits_for_review_despite_an_explicit_choice(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            row = group()
            key, review = self.evidence(root, row)
            pending, queue = activate_groups([row], [key], [], root, set())
            self.assertIn("sourceKey", pending[0]["items"][0])
            self.assertNotIn("key", pending[0]["items"][0])
            self.assertEqual("AWAITING_REVIEW", queue[0]["status"])
            graded, queue = activate_groups([row], [key], [review], root, set())
            item = graded[0]["items"][0]
            self.assertEqual(2, item["key"]["choice"])
            self.assertNotIn("explanation", item["key"])
            self.assertEqual([], queue)

    def test_wrong_source_version_or_changed_choices_cannot_activate(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            row = group()
            key, review = self.evidence(root, row)
            for modified, changed_key, changed_review in (
                (row, {**key, "source": "https://study4.com/another-test/"}, review),
                (row, {**key, "evidenceUrl": "https://study4.com/another-test/"}, review),
                (row, key, {**review, "version": "b" * 64}),
                (row, key, {**review, "label": "B"}),
                ({**row, "version": "c" * 64}, key, review),
                ({**row, "items": [{**row["items"][0], "choices": ["Two", "One", "Three", "Four"]}]}, key, review),
            ):
                active, queue = activate_groups([modified], [changed_key], [changed_review], root, set())
                self.assertNotIn("key", active[0]["items"][0])
                self.assertEqual(1, len(queue))

    def test_corrupt_evidence_or_duplicate_key_stays_ungraded(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            row = group()
            key, review = self.evidence(root, row)
            activated, queue = activate_groups([row], [key, {**key, "label": "A"}], [review], root, set())
            self.assertNotIn("sourceKey", activated[0]["items"][0])
            (root / f"{key['evidenceSha256']}.bin").write_bytes(b"Wrong source bytes")
            activated, queue = activate_groups([row], [key], [review], root, set())
            self.assertNotIn("sourceKey", activated[0]["items"][0])

    def test_withdrawing_group_leaves_input_snapshot_and_media_untouched(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "old.png").write_bytes(png())
            row = group()
            initial = deepcopy(row)
            active, queue = activate_groups([row], [], [], root, {row["id"]})
            self.assertEqual(([], []), (active, queue))
            self.assertEqual(initial, row)
            self.assertEqual(png(), (root / "old.png").read_bytes())

    def test_duplicate_item_or_group_cannot_enter_the_practice_bank(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            row = group()
            for rows in ([row, row], [row, {**row, "id": "other"}]):
                with self.assertRaisesRegex(ValueError, "Duplicate"):
                    activate_groups(rows, [], [], root, set())

    def test_missing_mp3_and_corrupt_image_fail_media_verification(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            old, new = root / "old", root / "new"
            old.mkdir()
            new.mkdir()
            image = package_media(png(), new, "image")
            verify_media({"image": image}, old, new)
            (new / Path(image["path"]).name).write_bytes(png()[:-2])
            with self.assertRaises(ValueError):
                verify_media({"image": image}, old, new)
            with self.assertRaises(FileNotFoundError):
                verify_media({"audio": {"path": "study_pack/media/missing.mp3"}}, old, new)

    def test_group_requires_exact_media_numbering_and_valid_sizes(self):
        record = {"question_id": 741, "is_grouped": True, "type": "listening",
                  "audio_url": "/wp-content/uploads/synthetic-part-3-32-34.mp3",
                  "sub_questions": [{"title": f"{i}. Listen", "choices": dict(zip("ABCD", "abcd"))} for i in (32, 33, 34)]}
        self.assertEqual(3, parse_candidate(record)[0])
        for invalid in ({**record, "audio_url": None},
                        {**record, "audio_url": "/wp-content/uploads/wrong-part-4-71-73.mp3"},
                        {**record, "sub_questions": record["sub_questions"][::-1]},
                        {**record, "part": 4}):
            with self.assertRaises(ValueError):
                parse_candidate(invalid)
