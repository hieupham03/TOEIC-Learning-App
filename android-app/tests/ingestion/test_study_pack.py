"""Synthetic Reading inputs only. Never opens the private cache."""
import html
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from test_listening_manifest import png
from prepare_study_pack import package_media, project_items, reading_record


def page(group_id=701, kind="reading", image="https://zenlishtoeic.vn/wp-content/uploads/synthetic.png"):
    group = {
        "question_id": group_id,
        "type": kind,
        "is_grouped": True,
        "content": html.escape(f'<img src="{image}">') if image else "",
        "sub_questions": [{
            "title": f"{i}. Synthetic question",
            "answer": [{"choice": label, "choice_answer": f"Example {label}"} for label in "ABCD"],
        } for i in (131, 132)],
    }
    return "<script>let data=" + json.dumps(group) + "</script>"


class StudyPackTests(unittest.TestCase):
    def test_reuses_exact_reading_image_and_keeps_question_order(self):
        questions, text, image = reading_record(page(), 701, 6, (131, 132))
        self.assertIsNone(text)
        self.assertTrue(image.endswith("/synthetic.png"))
        self.assertEqual([q["number"] for q in project_items(questions)], [131, 132])
        self.assertNotIn("key", project_items(questions)[0])

    def test_group_rejects_missing_or_foreign_passage(self):
        for value in (None, "https://synthetic.invalid/foreign.png"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                reading_record(page(image=value), 701, 6, (131, 132))

    def test_group_rejects_wrong_part_order(self):
        with self.assertRaises(ValueError):
            reading_record(page(), 701, 6, (132, 131))

    def test_media_path_is_content_addressed_and_type_checked(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            asset = package_media(png(), root, "image")
            self.assertTrue(asset["path"].endswith(asset["sha256"] + ".png"))
            self.assertTrue((root / Path(asset["path"]).name).is_file())
            with self.assertRaises(ValueError):
                package_media(png(), root, "audio")
