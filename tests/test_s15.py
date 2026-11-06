import unittest
from ezl.s05_blame import Tree
from ezl.s15_driver import goal_y
from _data import data

class TestDriver(unittest.TestCase):
  def test_one_goal_tree_splits_that_goal(self):
    d = data(); g = d.y[0]; t = Tree(d, d.rows, goal_y(g))
    self.assertIsNotNone(t.c)
    lo, hi = sorted([t.yes, t.no], key=lambda k: k.mu)
    self.assertLess(lo.mu, hi.mu)
