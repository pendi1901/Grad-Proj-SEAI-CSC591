import unittest
from ezl.s05_blame import Tree
from ezl.s08_fix import fix
from _data import data

class TestToBest(unittest.TestCase):
  def test_target_is_the_best_leaf(self):
    d = data(); t = Tree(d, d.rows); best = min(l.mu for l in t.leaves())
    _, leaf = fix(d, d.rows[0], t, best)
    self.assertEqual(leaf.mu, best)

  def test_tight_keeps_the_strictest(self):
    from ezl.s18_tobest import tight
    d = data(); c = d.x[0]
    self.assertEqual(tight([(c, 7, True), (c, 3, True), (c, 1, False)]), [(c, 3, True), (c, 1, False)])
