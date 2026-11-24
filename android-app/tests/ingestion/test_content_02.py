"""Synthetic source, review, and owner-bundle regression tests."""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from test_listening_manifest import png
from activate_study_content import activate_groups, item_binding
from acquire_study_content import parse_study_record, write_json
from extend_study_content import ReceiptClient
from listening_manifest import read_json
from prepare_study_pack import package_media
from review_study_content import check_disjoint, export_key_request, key_request_rows, owner_groups, review_rows, source_host
from study_review_page import render_review

SOURCE_URL = "https://publisher.invalid/workbook"


def reading_group(version="b" * 64):
    return {"id": "fixture-g", "part": 5, "version": version, "source": SOURCE_URL, "items": [
        {"id": "fixture-q", "number": 101, "prompt": "Fixture question", "choices": ["One", "Two", "Three", "Four"]},
    ]}


def evidence(root, group, status):
    data = b"Synthetic source edition. Fixture question: choice B."
    digest = sha256(data).hexdigest()
    (root / f"{digest}.bin").write_bytes(data)
    return {**item_binding(group, group["items"][0]), "status": status, "label": "B",
            "reviewer": "Synthetic reviewer", "reviewedAt": "2026-11-22", "evidenceUrl": SOURCE_URL,
            "evidenceSha256": digest, "locator": "Page 1, item 101"}


class Content02Tests(unittest.TestCase):
    def test_source_only_approved_then_revoked_without_rewriting_snapshot(self):
        with TemporaryDirectory() as work:
            root = Path(work)
            group = reading_group()
            row = evidence(root, group, "SOURCE_ONLY")
            records = review_rows([row], [group], root)
            pending, queue = activate_groups([group], records, records, root, set(), source_host=source_host)
            self.assertEqual("AWAITING_REVIEW", queue[0]["status"])
            self.assertNotIn("key", pending[0]["items"][0])
            approved = {**row, "status": "APPROVED", "explanation": "Fixture explanation", "explanationLocator": "Page 2"}
            checked = review_rows([approved], [group], root)
            snapshot, _ = activate_groups([group], checked, checked, root, set(), source_host=source_host)
            self.assertEqual(1, snapshot[0]["items"][0]["key"]["choice"])
            self.assertEqual("Fixture explanation", snapshot[0]["items"][0]["key"]["explanation"])
            self.assertNotIn("batchAccepted", snapshot[0]["items"][0]["key"])
            batch = review_rows([{**approved, "reviewScope": "PO_BATCH_ACCEPTANCE"}], [group], root)
            accepted, _ = activate_groups([group], checked, batch, root, set(), source_host=source_host)
            self.assertTrue(accepted[0]["items"][0]["key"]["batchAccepted"])
            self.assertEqual(snapshot[0]["items"][0]["sourceKey"], accepted[0]["items"][0]["sourceKey"])
            revoked = review_rows([{**row, "status": "REVOKED"}], [group], root)
            current, queue = activate_groups([group], revoked, revoked, root, set(), source_host=source_host)
            self.assertEqual("REVOKED", queue[0]["status"])
            self.assertNotIn("key", current[0]["items"][0])
            self.assertEqual(1, snapshot[0]["items"][0]["key"]["choice"])

    def test_reviews_reject_stale_source_group_media_and_document(self):
        with TemporaryDirectory() as work:
            root = Path(work)
            group = reading_group()
            row = evidence(root, group, "APPROVED")
            variants = []
            for key, value in (("id", "another"), ("version", "d" * 64), ("source", "https://wrong.invalid/item"),
                               ("audio", {"sha256": "e" * 64}), ("extraImages", [{"sha256": "9" * 64}])):
                variants.append({**group, key: value})
            variants += [{**group, "items": [{**group["items"][0], key: value}]}
                         for key, value in (("prompt", "Changed stem"), ("choices", ["Two", "One", "Three", "Four"]))]
            for changed in variants:
                with self.assertRaises(ValueError):
                    review_rows([row], [changed], root)
            for change in ({"reviewer": ""}, {"reviewedAt": ""}, {"label": "E"},
                           {"evidenceUrl": "https://foreign.invalid/key"}, {"evidenceSha256": "0" * 64}):
                with self.assertRaises(ValueError):
                    review_rows([{**row, **change}], [group], root)
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                review_rows([row, row], [group], root)
            second = {**group, "id": "other", "items": [{**group["items"][0], "id": "two", "number": 102}]}
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                review_rows([row, {**row, **item_binding(second, second["items"][0])}], [group, second], root)
            (root / f"{row['evidenceSha256']}.bin").write_bytes(b"corrupt")
            with self.assertRaises(ValueError):
                review_rows([row], [group], root)

    def test_owner_import_checks_panel_order_bytes_linkage_and_mock_overlap(self):
        with TemporaryDirectory() as work:
            base = Path(work)
            owner = base / "owner"
            for directory in ("sources", "media"):
                (owner / directory).mkdir(parents=True)
            active_media = base / "pack-media"
            active_media.mkdir()
            data = b"Synthetic captured practice source"
            version = sha256(data).hexdigest()
            (owner / "sources" / f"{version}.bin").write_bytes(data)
            group = reading_group(version)
            group.update(part=7, items=[
                {"id": f"fixture-{i}", "number": i, "prompt": f"Fixture question {i}",
                 "choices": ["One", "Two", "Three", "Four"]} for i in (147, 148)])
            photo = package_media(png(), owner / "media", "image")
            group.update(image=photo, imageItems=["fixture-147", "fixture-148"])
            file = owner / "bundle.json"
            bundle = {"schema": 1, "practice": [group], "inventories": []}
            write_json(file, bundle)
            practice, forms = owner_groups(owner, [], active_media)
            self.assertEqual([group], practice)
            self.assertFalse(forms)
            self.assertEqual(png(), (active_media / Path(photo["path"]).name).read_bytes())
            write_json(file, {**bundle, "inventories": [{"id": "A", "groups": [group]}]})
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                owner_groups(owner, [], active_media)
            write_json(file, {**bundle, "practice": [{**group, "imageItems": ["fixture-148", "fixture-147"]}]})
            with self.assertRaisesRegex(ValueError, "ordered item IDs"):
                owner_groups(owner, [], active_media)
            write_json(file, bundle)
            (owner / "media" / Path(photo["path"]).name).write_bytes(png()[:-6])
            with self.assertRaises(ValueError):
                owner_groups(owner, [], active_media)

    def test_source_parser_keeps_ordered_group_panels_and_does_not_promote_options(self):
        group = {"question_id": 500, "is_grouped": True, "type": "reading",
                 "content": '<img src="/wp-content/uploads/b.png"><img src="/wp-content/uploads/a.png">',
                 "sub_questions": [{"title": f"{i}. Synthetic", "answer": [
                     {"choice": label, "choice_answer": label} for label in "ABCD"]} for i in (147, 148)]}
        _, questions, _, _, images = parse_study_record(group)
        self.assertEqual(["b.png", "a.png"], [url.rsplit("/", 1)[-1] for url in images])
        self.assertTrue(all(q["answer"]["label"] is None for q in questions))
        changed = deepcopy(group)
        changed["sub_questions"][0]["image_url"] = "/wp-content/uploads/item-only.png"
        with self.assertRaisesRegex(ValueError, "Question-specific"):
            parse_study_record(changed)

    def test_disjoint_corpus_validation_detects_choice_reordering(self):
        first = reading_group()
        second = reading_group("5" * 64)
        second["id"] = "synthetic-other-group"
        second["items"][0].update(id="synthetic-other-item", choices=["Four", "One", "Two", "Three"])
        with self.assertRaisesRegex(ValueError, "Duplicate question"):
            check_disjoint([first, second])

    def test_resume_keeps_interrupted_request_charge_and_access_stop(self):
        with TemporaryDirectory() as work:
            ledger = Path(work) / "ledger.json"
            write_json(ledger, {"http": [{"status": None, "bytes": 100, "interrupted": True},
                                         {"status": 429, "bytes": 0}], "stop_reason": None})
            client = ReceiptClient(ledger)
            self.assertEqual((2, 100), (client.requests, client.downloaded))
            self.assertEqual("HTTP 429 — source stopped", client.stop_reason)

    def test_key_request_export_keeps_exact_binding_and_separates_reading_from_listening(self):
        with TemporaryDirectory() as work:
            root = Path(work)
            reading = reading_group()
            listening = {**reading_group(), "part": 2, "id": "second", "items": [
                {"id": "listening-item", "number": 10, "prompt": "", "choices": ["A", "B", "C"]}]}
            groups = [listening, reading]
            queue = [{**item_binding(group, group["items"][0]), "part": group["part"],
                      "number": group["items"][0]["number"], "status": "SOURCE_EVIDENCE_REQUIRED"} for group in groups]
            pack = root / "assets/study_pack/pack.json"
            pack.parent.mkdir(parents=True)
            write_json(pack, {"schema": 1, "practice": groups})
            original = pack.read_bytes()
            write_json(root / "activation.json", {"pack_sha256": sha256(original).hexdigest()})
            write_json(root / "answer-review-queue.json", queue)
            result = export_key_request(root, root / "request")
            self.assertEqual((1, 1), (result["reading"], result["listening"]))
            for part, name in ((5, "01-reading-key-request.json"), (2, "02-listening-key-request.json")):
                path = root / "request" / name
                row = next(row for row in key_request_rows(groups, queue) if row["part"] == part)
                self.assertEqual([row], read_json(path))
                self.assertEqual("", row["label"])
                with self.assertRaises(ValueError):
                    review_rows([row], groups, root)
            reading_row = read_json(root / "request/01-reading-key-request.json")[0]
            source = evidence(root, reading, "SOURCE_ONLY")
            for field in ("label", "reviewer", "reviewedAt", "evidenceUrl", "evidenceSha256", "locator"):
                reading_row[field] = source[field]
            checked = review_rows([reading_row], groups, root)
            active, _ = activate_groups(groups, checked, checked, root, set(), source_host=source_host)
            item = active[1]["items"][0]
            self.assertIn("sourceKey", item)
            self.assertNotIn("key", item)
            self.assertEqual(original, pack.read_bytes())

    def test_key_request_rejects_missing_duplicate_or_stale_rows(self):
        group = reading_group()
        item = group["items"][0]
        row = {**item_binding(group, item), "part": group["part"], "number": item["number"], "status": "AWAITING_REVIEW"}
        for rows in ([], [row, row], [{**row, "number": 102}], [{**row, "itemSha256": "0" * 64}]):
            with self.assertRaises(ValueError):
                key_request_rows([group], rows)
        group["items"][0]["choices"] = item["choices"][::-1]
        with self.assertRaises(ValueError):
            key_request_rows([group], [row])

    def test_review_page_keeps_question_text_in_data_instead_of_executable_markup(self):
        with TemporaryDirectory() as work:
            path = Path(work) / "review.html"
            group = reading_group()
            group["items"][0]["prompt"] = "</script><script>never run</script>"
            render_review(path, [group], [], [])
            page = path.read_text(encoding="utf-8")
            self.assertIn("fixture-q", page)
            self.assertNotIn("</script><script>never run", page)
            self.assertIn("default-src 'none'", page)
