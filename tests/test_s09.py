import unittest
from ezl.s09_spot import oddness
from _data import data

class TestSpot(unittest.TestCase):
  def test_a_planted_oddball_is_odder(self):
    d = data(); ref = d.rows[:100]
    odd = list(d.rows[0])
    for c in d.x: odd[c.at] = c.mu + 10 * c.div()  # pom3a is all numeric
    self.assertGreater(oddness(d, odd, ref), max(oddness(d, r, ref) for r in d.rows[100:150]))
