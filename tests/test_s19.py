import unittest
from ezl.s19_surprise import surprise
from _data import data

class TestSurprise(unittest.TestCase):
  def test_a_planted_flop_is_surprising(self):
    d = data(); flop = list(d.rows[0])
    for c in d.y: flop[c.at] = 1 - c.heaven  # worst possible goals
    d.rows.append(flop)
    self.assertGreater(surprise(d, flop), max(surprise(d, r) for r in d.rows[1:20]))
