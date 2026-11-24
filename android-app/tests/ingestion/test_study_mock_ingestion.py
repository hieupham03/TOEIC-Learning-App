"""Synthetic end-to-end checks for the existing review and mock intake paths."""
from hashlib import sha256
from pathlib import Path
import struct
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
import zlib

from test_zenlish_crawler import frames
from activate_study_content import item_binding
from acquire_study_content import PART_ENDS
from extend_study_content import save_json
from listening_manifest import read_json
from prepare_study_pack import package_media
from review_study_content import assemble, export_key_request


def photo(value):
    def chunk(kind, body):
        return struct.pack(">I", len(body)) + kind + body + struct.pack(">I", zlib.crc32(kind + body))
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", 1, 1, 8, 0, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(bytes((0, value)))) + chunk(b"IEND", b""))


def synthetic_edition(slot, owner, evidence):
    version = sha256(f"Synthetic paper {slot}".encode()).hexdigest()
    (owner / "sources" / f"{version}.bin").write_text(f"Synthetic paper {slot}", encoding="ascii")
    answer_text = f"Synthetic key {slot}".encode()
    answer_sha = sha256(answer_text).hexdigest()
    (evidence / f"{answer_sha}.bin").write_bytes(answer_text)
    source = f"https://publisher.invalid/fixture-{slot}"
    groups, keys = [], []
    for part, (start, end) in enumerate(zip((0, *PART_ENDS[:-1]), PART_ENDS), 1):
        size = {3: 3, 4: 3, 6: 4, 7: 2}.get(part, 1)
        for first in range(start + 1, end + 1, size):
            group_id = f"{slot}-{first}"
            items = [{"id": f"{slot}-q{n}", "number": n, "prompt": f"Fixture question {slot} {n}",
                      "choices": list("ABC" if part == 2 else "ABCD")} for n in range(first, first + size)]
            ids = [item["id"] for item in items]
            group = {"id": group_id, "part": part, "source": source, "version": version, "items": items}
            if part <= 4:
                clip = frames()
                payload = clip[:15] + group_id.encode() + clip[15 + len(group_id):]
                group.update(audio=package_media(payload, owner / "media", "audio"), audioItems=ids)
            if part == 1:
                group.update(image=package_media(photo(first + (0 if slot == "A" else 10)), owner / "media", "image"),
                             imageItems=ids)
            if part >= 6:
                group.update(passage=f"Fixture passage {group_id}", passageItems=ids)
            groups.append(group)
            keys.extend({**item_binding(group, item), "label": "A", "evidenceUrl": source + "/key",
                         "evidenceSha256": answer_sha, "locator": f'{slot} row {item["number"]}'} for item in items)
    return {"id": slot, "groups": groups}, keys


class MockIngestionTests(unittest.TestCase):
    def test_pair_requires_independent_source_keys_item_reviews_and_both_form_reviews(self):
        with TemporaryDirectory() as work:
            root = Path(work)
            owner, evidence = root / "owner", root / "source-evidence"
            for folder in (owner / "sources", owner / "media", evidence):
                folder.mkdir(parents=True, exist_ok=True)
            save_json(root / "new-groups.json", [])
            a, a_keys = synthetic_edition("A", owner, evidence)
            b, b_keys = synthetic_edition("B", owner, evidence)
            bundle = {"schema": 1, "practice": [], "inventories": [a, b]}
            save_json(owner / "bundle.json", bundle)
            qa = b"Synthetic form QA document"
            qa_sha = sha256(qa).hexdigest()
            (evidence / f"{qa_sha}.bin").write_bytes(qa)
            decisions = [{**key, "reviewer": "Synthetic reviewer", "reviewedAt": "2026-11-24", "status": "APPROVED"}
                         for key in a_keys + b_keys]
            review_file = root / "synthetic-decisions.json"
            save_json(review_file, decisions)
            with patch("review_study_content.seed_previous", return_value={"practice": []}), \
                    patch("review_study_content.snapshot_source", return_value=b""), \
                    patch("review_study_content.source_keys", return_value=[]):
                no_keys = assemble(root, review_file=review_file)
                self.assertEqual(0, no_keys["mock_inventory"]["A"]["reviewed"])
                self.assertEqual([], no_keys["published_forms"])
                save_json(owner / "source-keys.json", a_keys + b_keys)
                save_json(review_file, [{**decisions[0], "reviewScope": "PO_BATCH_ACCEPTANCE"}])
                batch = assemble(root, review_file=review_file)
                self.assertEqual((200, 199, "ITEM_REVIEW_REQUIRED"), (
                    batch["mock_inventory"]["A"]["source_keys"], batch["mock_inventory"]["A"]["reviewed"],
                    batch["mock_inventory"]["A"]["status"],
                ))
                self.assertEqual([], batch["published_forms"])
                save_json(review_file, [decisions[0]])
                assemble(root, review_file=review_file)
                checked = assemble(root)
                for form in (a, b):
                    status = checked["mock_inventory"][form["id"]]
                    self.assertEqual((200, 200, "FORM_REVIEW_REQUIRED"),
                                     (status["source_keys"], status["reviewed"], status["status"]))
                    form["review"] = {"status": "APPROVED", "reviewer": "Synthetic reviewer",
                                      "reviewedAt": "2026-11-24", "formSha256": status["form_sha256"],
                                      "evidenceUrl": "https://publisher.invalid/qa", "evidenceSha256": qa_sha,
                                      "locator": f'QA fixture for {form["id"]}'}
                b_review = b.pop("review")
                save_json(owner / "bundle.json", bundle)
                one = assemble(root)
                self.assertEqual("FORM_READY", one["mock_inventory"]["A"]["status"])
                self.assertEqual([], one["published_forms"])
                b["review"] = {**b_review, "formSha256": "0" * 64}
                save_json(owner / "bundle.json", bundle)
                self.assertEqual([], assemble(root)["published_forms"])
                b["review"] = b_review
                save_json(owner / "bundle.json", bundle)
                self.assertEqual(["A", "B"], assemble(root)["published_forms"])
                pack_path = root / "assets/study_pack/pack.json"
                self.assertEqual([200, 200], [sum(len(g["items"]) for g in f["groups"]) for f in read_json(pack_path)["forms"]])
                self.assertEqual(120, len(list(pack_path.parent.joinpath("media").iterdir())))
                self.assertEqual(0, export_key_request(root, root / "key-request")["reading"])
                b["review"]["status"] = "REVOKED"
                save_json(owner / "bundle.json", bundle)
                self.assertEqual([], assemble(root)["published_forms"])
                self.assertNotIn("forms", read_json(pack_path))
                self.assertFalse(list(pack_path.parent.joinpath("media").iterdir()))

    def test_review_queue_keeps_partial_inventory_separate_from_practice_export(self):
        with TemporaryDirectory() as work:
            root = Path(work)
            owner, evidence = root / "owner", root / "source-evidence"
            for folder in (owner / "sources", owner / "media", evidence):
                folder.mkdir(parents=True, exist_ok=True)
            form, keys = synthetic_edition("A", owner, evidence)
            form["groups"] = form["groups"][:1]
            save_json(root / "new-groups.json", [])
            save_json(owner / "bundle.json", {"schema": 1, "practice": [], "inventories": [form]})
            save_json(owner / "source-keys.json", keys[:1])
            with patch("review_study_content.seed_previous", return_value={"practice": []}), \
                    patch("review_study_content.snapshot_source", return_value=b""), \
                    patch("review_study_content.source_keys", return_value=[]):
                report = assemble(root)
            self.assertEqual("STRUCTURE_INCOMPLETE", report["mock_inventory"]["A"]["status"])
            self.assertEqual([], report["published_forms"])
            row, = read_json(root / "answer-review-queue.json")
            self.assertEqual(("A", "AWAITING_REVIEW"), (row["form"], row["status"]))
            self.assertEqual(0, export_key_request(root, root / "key-request")["listening"])
            self.assertIn('"form": "A"', (root / "review.html").read_text(encoding="utf-8"))
