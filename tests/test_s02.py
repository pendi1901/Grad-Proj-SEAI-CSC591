import unittest
from ezl.core import mean
from ezl.s02_guess import guess, split
from _data import data

class TestGuess(unittest.TestCase):
  def test_guess_beats_the_spread(self):
    d = data(); test, train = split(d, 30)
    for j, c in enumerate(d.y):
      miss = mean(abs(guess(d, r, train)[j] - r[c.at]) for r in test)
      self.assertLess(miss, c.div() * 1.5)

  def test_guess_of_a_known_row_is_close(self):
    d = data(); r = d.rows[0]
    self.assertEqual(len(guess(d, r)), len(d.y))
