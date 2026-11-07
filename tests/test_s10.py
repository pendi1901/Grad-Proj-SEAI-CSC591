import io, unittest
from contextlib import redirect_stdout
from ezl.s10_race import ask10, verdict
from _data import data

class TestRace(unittest.TestCase):
  def test_race_gives_a_verdict(self):
    out = io.StringIO()
    with redirect_stdout(out): ask10(data())
    self.assertIn("verdict:", out.getvalue())

  def test_equal_medians_are_not_a_win(self):
    ours, rand = [100]*15 + [90]*5, [100]*15 + [0]*5
    self.assertIn("medians tie", verdict(ours, rand))
    self.assertEqual(verdict([1]*20, [1]*20), "a tie: no real difference")
