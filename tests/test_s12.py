import io, re, unittest
from contextlib import redirect_stdout
from ezl.s12_range import ask12
from _data import data

class TestRange(unittest.TestCase):
  def test_ranges_usually_hold_the_truth(self):
    out = io.StringIO()
    with redirect_stdout(out): ask12(data())
    pcts = [int(p) for p in re.findall(r"inside the range (\d+)%", out.getvalue())]
    self.assertEqual(len(pcts), 3)
    self.assertGreater(min(pcts), 50)
