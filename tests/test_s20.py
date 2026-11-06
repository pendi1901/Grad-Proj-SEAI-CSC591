import io, unittest
from contextlib import redirect_stdout
from ezl.s20_vsmean import ask20
from _data import data

class TestVsMean(unittest.TestCase):
  def test_one_verdict_per_goal(self):
    out = io.StringIO()
    with redirect_stdout(out): ask20(data())
    self.assertEqual(out.getvalue().count("->"), 3)
