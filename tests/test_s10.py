import io, unittest
from contextlib import redirect_stdout
from ezl.s10_race import ask10
from _data import data

class TestRace(unittest.TestCase):
  def test_race_gives_a_verdict(self):
    out = io.StringIO()
    with redirect_stdout(out): ask10(data())
    self.assertIn("verdict:", out.getvalue())
