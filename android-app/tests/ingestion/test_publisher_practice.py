"""Synthetic publisher layout and source-to-review regressions."""
from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from activate_study_content import activate_groups
from prepare_publisher_practice import (
    FAUST_PAPER, englishclub_memo, faust_part5, faust_public_keys, faust_revision,
    groups_with_keys, publisher_file,
)
from review_study_content import publisher_key_rows, review_rows, source_host


class PublisherPracticeTests(unittest.TestCase):
    def test_question_and_key_pdfs_require_same_edition(self):
        revision = '169ed3c0-b2a9-41d1-8a78-d67451601c9b'
        edition = f'{FAUST_PAPER}/revisions/{revision}'
        self.assertEqual(revision, faust_revision(f'{edition}/candidate.pdf', f'{edition}/teacher.pdf', FAUST_PAPER))
        with self.assertRaisesRegex(ValueError, 'revision'):
            faust_revision(f'{edition}/candidate.pdf', f'{edition.replace("01c9b", "01c9a")}/teacher.pdf', FAUST_PAPER)

    def test_paper_order_and_partial_key(self):
        questions = '\n'.join(f'{number}. Synthetic item {number}\n(A) One\n(B) Two\n(C) Three\n(D) Four'
                              for number in range(101, 131))
        cover = 'Part 5\nQuestions 101 to 130\nPart 6'
        start, continuation = questions.split('\n120.', 1)
        pages = [cover, f'Part 5\n{start}', f'Faust\n3\nfaustacademy.com/fixture\nFAUST ACADEMY fixture\n120.{continuation}',
                 'Part 6\n131. Other item']
        items = faust_part5(pages)
        self.assertEqual(list(range(101, 131)), list(items))
        self.assertEqual(('Synthetic item 101', ['One', 'Two', 'Three', 'Four']), items[101])
        self.assertEqual('Four', items[119][1][3])
        self.assertEqual({101: ('C', 'PDF page 1, question 101')}, faust_public_keys(['101: C', 'Preview'], items))
        with self.assertRaisesRegex(ValueError, 'Duplicate|duplicate'):
            faust_public_keys(['101: C', '101: B'], items)
        with self.assertRaisesRegex(ValueError, 'order'):
            faust_part5([page.replace('(A) One\n(B) Two', '(B) Two\n(A) One', 1) for page in pages])

    def test_reading_memo_binds_passage_and_numbered_questions(self):
        html = '<h2>Example 1: Memo</h2><div class="clr-blue">A fictional office memo.</div>'
        for number, answer in ((1, 'A'), (2, 'C')):
            html += (f'<p class="clr-blue">{number}. Synthetic item {number}</p>'
                     f'<p class="clr-blue">A) One<br>B) Two<br>C) Three<br>D) Four</p>'
                     f'<p>The correct answer is <b>{answer}</b>.</p>')
        html += '<h2>Example 2: Other</h2>'
        passage, items, keys = englishclub_memo(html)
        self.assertEqual('A fictional office memo.', passage)
        self.assertEqual([1, 2], [item['number'] for item in items])
        self.assertEqual({1: 'A', 2: 'C'}, keys)
        with self.assertRaisesRegex(ValueError, 'order'):
            englishclub_memo(html.replace('>2. Synthetic', '>1. Synthetic'))

    def test_download_receipt_requires_exact_file_bytes(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            body = b'Fixture downloaded receipt'
            digest = sha256(body).hexdigest()
            receipt = {'test.pdf': {'sha256': digest, 'url': FAUST_PAPER, 'bytes': len(body)}}
            target = root / 'test.pdf'
            target.write_bytes(body)
            self.assertEqual((body, FAUST_PAPER, digest), publisher_file(root, receipt, target.name))
            target.write_bytes(b'x' * len(body))
            with self.assertRaisesRegex(ValueError, 'receipt'):
                publisher_file(root, receipt, target.name)

    def test_publisher_key_remains_pending_until_independent_matching_review(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            body = b'Synthetic key fixture'
            digest = sha256(body).hexdigest()
            path = root / f'{digest}.bin'
            path.write_bytes(body)
            groups, rows = groups_with_keys('fixture', FAUST_PAPER, '8' * 64, FAUST_PAPER, digest,
                                           {101: ('Synthetic question', ['One', 'Two', 'Three', 'Four'])},
                                           {101: ('B', 'Synthetic page item 101')})
            published = publisher_key_rows(rows, groups, root)
            review = {**rows[0], 'status': 'APPROVED', 'reviewer': 'Synthetic reviewer', 'reviewedAt': '2026-11-22'}
            cases = [([], 'AWAITING_REVIEW'), ([{**review, 'label': 'C'}], 'REVIEW_REJECTED_OR_MISMATCH'),
                     ([review], None)]
            for decisions, status in cases:
                with self.subTest(status=status):
                    valid_reviews = review_rows(decisions, groups, root)
                    active, queue = activate_groups(groups, published, valid_reviews, root, set(), source_host=source_host)
                    item = active[0]['items'][0]
                    self.assertEqual(1, item['sourceKey']['choice'])
                    if status is None:
                        self.assertEqual(1, item['key']['choice'])
                        self.assertEqual([], queue)
                    else:
                        self.assertNotIn('key', item)
                        self.assertEqual(status, queue[0]['status'])
            with self.assertRaisesRegex(ValueError, 'Duplicate'):
                publisher_key_rows(rows * 2, groups, root)
            path.write_bytes(b'Changed evidence')
            with self.assertRaisesRegex(ValueError, 'evidence'):
                publisher_key_rows(rows, groups, root)
