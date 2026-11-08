import unittest
from ezl.core import the, median
from ezl.s05_blame import Tree
from ezl.s08_fix import fix

class TestFix(unittest.TestCase):
  def test_fix_lands_in_a_good_branch(self):
    from _data import data
    d = data(); t = Tree(d, d.rows); row = max(d.rows, key=d.disty)
    goal = median(map(d.disty, d.rows))
    changes, leaf = fix(d, row, t, goal)
    self.assertLessEqual(leaf.mu, goal)
    self.assertGreater(len(changes), 0)

  def test_fix_only_touches_allowed_columns(self):
    from _data import data
    d = data(); t = Tree(d, d.rows); row = max(d.rows, key=d.disty)
    goal = median(map(d.disty, d.rows)); old = the["change"]
    try:
      the["change"] = "Plan,Size,Team Size"
      got = fix(d, row, t, goal)
      if got: self.assertTrue(all(k[0].name in the["change"].split(",") for k in got[0]))
      the["change"] = "nosuchcolumn"
      self.assertIsNone(fix(d, row, t, goal))
    finally: the["change"] = old
