import unittest
from ezl.core import median
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
