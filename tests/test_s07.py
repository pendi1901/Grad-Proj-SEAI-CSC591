import unittest
from ezl.core import median
from ezl.s07_choose import acquire, choose, wins
from _data import data

class TestChoose(unittest.TestCase):
  def test_acquire_spends_the_budget_exactly(self):
    d = data(); lab = acquire(d, d.rows, 20)
    self.assertEqual(len(lab), 20)
    self.assertEqual(len({id(r) for r in lab}), 20)

  def test_choose_beats_the_median_row(self):
    d = data(); win = wins(d)
    self.assertGreater(median(win(choose(d, budget=30)) for _ in range(5)), 0)

  def test_acquire_ends_when_budget_nearly_equals_rows(self):
    d = data(); rows = d.rows[:46]
    self.assertEqual(len(acquire(d, rows, 45)), 45)
    self.assertEqual(len(acquire(d, rows, 99)), 46)
