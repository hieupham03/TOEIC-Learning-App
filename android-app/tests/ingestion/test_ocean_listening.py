import unittest

from prepare_ocean_listening import flat_bank, ordered_question, speech_turns


class OceanListeningTests(unittest.TestCase):
    def test_only_flat_literal_bank_is_accepted(self):
        self.assertEqual([{"id": "fixture"}], flat_bank(b'window.BUILTIN_BANK = [{"id":"fixture"}];'))
        with self.assertRaises(ValueError):
            flat_bank(b'window.BUILTIN_BANK = [{"id":"fixture"}]; alert("extra");')

    def test_spoken_choice_labels_and_correct_index_are_changed_together(self):
        row = {"id": "P2-fixture", "audioText": "What did you order?", "choices": ["A book.", "At noon.", "In a box."],
               "answer": 0}
        item, key, order = ordered_question(row, 7, spoken_slot=2)
        self.assertEqual([1, 2, 0], order)
        self.assertEqual(2, key)
        turns = speech_turns(2, row, [item])
        self.assertEqual(("W", "What did you order?"), turns[0])
        self.assertEqual("Choice C. A book.", turns[1 + key][1])

    def test_dialogue_keeps_author_speaker_turns_and_three_stems(self):
        row = {"audioText": "W: Is the room ready? M: It is. W: Thanks."}
        questions = [{"number": n, "prompt": f"Fixture {n}?"} for n in (4, 5, 6)]
        turns = speech_turns(3, row, questions)
        self.assertEqual([("W", "Is the room ready?"), ("M", "It is."), ("W", "Thanks.")], turns[:3])
        self.assertEqual(["Question 4. Fixture 4?", "Question 5. Fixture 5?", "Question 6. Fixture 6?"],
                         [text for _, text in turns[3:]])
