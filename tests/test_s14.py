import unittest
from ezl.s14_drift import drift
from _data import data

class TestDrift(unittest.TestCase):
  def test_sorted_by_score_drifts_and_shuffled_does_not(self):
    d = data()
    self.assertIsNotNone(drift(d, sorted(d.rows, key=d.disty), 50))
    self.assertIsNone(drift(d, d.rows, 120))
