import unittest
from ezl.core import mean
from ezl.s04_flow import stream
from _data import data

class TestFlow(unittest.TestCase):
  def test_flagged_rows_really_are_better(self):
    d = data(); got = list(stream(d, d.rows))
    self.assertEqual(len(got), len(d.rows) - 32)
    yes = [r for r, w in got if w]
    self.assertTrue(yes)
    self.assertLess(mean(map(d.disty, yes)), mean(map(d.disty, d.rows)))
