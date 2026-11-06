import unittest
from ezl.s03_certify import holds
from ezl.s05_blame import Tree
from ezl.s16_why import why
from _data import data

class TestWhy(unittest.TestCase):
  def test_reasons_are_true_of_the_row(self):
    d = data(); t = Tree(d, d.rows)
    for row in d.rows[:10]:
      conds, leaf = why(t, row)
      self.assertTrue(conds)
      self.assertTrue(all(holds(c, row[c.at], v) == yes for c, v, yes in conds))
