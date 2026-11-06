import unittest
from ezl.s05_blame import Tree
from _data import data

class TestBlame(unittest.TestCase):
  def test_leaves_partition_rows(self):
    d = data(); t = Tree(d, d.rows)
    self.assertIsNotNone(t.c)
    self.assertEqual(sum(len(l.rows) for l in t.leaves()), len(d.rows))

  def test_every_row_walks_to_its_own_leaf(self):
    d = data(); t = Tree(d, d.rows)
    for r in d.rows[:20]: self.assertTrue(any(r is x for x in t.leaf(r).rows))

  def test_best_leaf_beats_root(self):
    d = data(); t = Tree(d, d.rows)
    self.assertLess(min(l.mu for l in t.leaves()), t.mu)
