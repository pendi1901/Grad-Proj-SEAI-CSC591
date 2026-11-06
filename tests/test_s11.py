import io, unittest
from contextlib import redirect_stdout
from ezl.s11_families import ask11
from _data import data

class TestFamilies(unittest.TestCase):
  def test_one_line_per_family(self):
    out = io.StringIO()
    with redirect_stdout(out): ask11(data())
    self.assertGreater(out.getvalue().count("family"), 2)
