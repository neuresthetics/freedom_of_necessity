import unittest

from rubric_parser import parse_judge, parse_score, strip_think

GOOD = """Some reasoning about L, H and B.
BEGIN_VERDICT
VERDICT L: NOT TRIGGERED
VERDICT H: **PARTLY TRIGGERED**
VERDICT B: not triggered
SCORE A5: 0.70
SCORE P3_OWN: 0.7
END_VERDICT
"""


class TestRubricParser(unittest.TestCase):
    def test_good_block(self):
        r = parse_judge(GOOD, ["L", "H", "B"], ["A5", "P3_OWN"])
        self.assertTrue(r["block_found"])
        self.assertEqual(r["verdicts"]["L"]["value"], "NOT TRIGGERED")
        self.assertEqual(r["verdicts"]["H"]["value"], "PARTLY TRIGGERED")
        self.assertEqual(r["verdicts"]["B"]["value"], "NOT TRIGGERED")
        self.assertEqual(r["scores"]["A5"]["value"], 0.70)
        self.assertEqual(r["scores"]["P3_OWN"]["value"], 0.70)

    def test_off_rubric_value_is_unparsed(self):
        for bad in ("0.72", "0.9", "1.0", "0.0", "seventy", "0.70 or 0.50", "70%", ""):
            self.assertIsNone(parse_score(bad), bad)
            text = "BEGIN_VERDICT\nSCORE A5: %s\nEND_VERDICT" % bad
            r = parse_judge(text, [], ["A5"])
            self.assertIn(r["scores"]["A5"]["status"], ("unparsed", "missing"), bad)
            self.assertIsNone(r["scores"]["A5"]["value"])

    def test_all_five_values(self):
        for v in ("0.85", "0.70", "0.50", "0.25", "0.10", ".5", "0.1"):
            self.assertIsNotNone(parse_score(v), v)

    def test_no_block_no_guessing(self):
        text = "I would score A5 at 0.70 and P3_OWN at 0.85. VERDICT L: TRIGGERED"
        r = parse_judge(text, ["L"], ["A5", "P3_OWN"])
        self.assertFalse(r["block_found"])
        self.assertEqual(r["scores"]["A5"]["status"], "missing")
        self.assertEqual(r["verdicts"]["L"]["status"], "missing")

    def test_conflicting_duplicates(self):
        text = "BEGIN_VERDICT\nSCORE A5: 0.70\nSCORE A5: 0.50\nEND_VERDICT"
        r = parse_judge(text, [], ["A5"])
        self.assertEqual(r["scores"]["A5"]["status"], "unparsed")

    def test_bad_verdict_word(self):
        text = "BEGIN_VERDICT\nVERDICT H: MOSTLY TRIGGERED\nEND_VERDICT"
        r = parse_judge(text, ["H"], [])
        self.assertEqual(r["verdicts"]["H"]["status"], "unparsed")

    def test_think_block_ignored(self):
        text = ("<think>BEGIN_VERDICT\nSCORE A5: 0.85\nEND_VERDICT</think>\n"
                "BEGIN_VERDICT\nSCORE A5: 0.25\nEND_VERDICT")
        self.assertNotIn("<think>", strip_think(text))
        r = parse_judge(text, [], ["A5"])
        self.assertEqual(r["scores"]["A5"]["value"], 0.25)

    def test_last_block_wins(self):
        text = ("BEGIN_VERDICT\nSCORE A5: <0.85|0.70|0.50|0.25|0.10>\nEND_VERDICT\n"
                "BEGIN_VERDICT\nSCORE A5: 0.50\nEND_VERDICT")
        r = parse_judge(text, [], ["A5"])
        self.assertEqual(r["scores"]["A5"]["value"], 0.50)


if __name__ == "__main__":
    unittest.main()
