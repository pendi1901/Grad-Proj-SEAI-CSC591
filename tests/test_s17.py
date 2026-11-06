import unittest
from ezl.s07_choose import choose
from ezl.s17_within import alike
from _data import data

class TestWithin(unittest.TestCase):
  def test_pick_keeps_the_fixed_settings(self):
    d = data(); fixed = d.x[:1]; ref = d.rows[0]
    rows = alike(d, ref, fixed, .3)
    self.assertTrue(any(r is ref for r in rows))
    pick = choose(d, rows, min(30, len(rows) // 2))
    self.assertLessEqual(fixed[0].dist(pick[fixed[0].at], ref[fixed[0].at]), .3)
