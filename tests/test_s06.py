import unittest
from ezl.s03_certify import holds
from ezl.s05_blame import Tree
from ezl.s06_justify import rules, say
from _data import data

class TestJustify(unittest.TestCase):
  def test_rules_are_true_of_their_rows(self):
    d = data()
    for conds, leaf in rules(Tree(d, d.rows)):
      for r in leaf.rows:
        self.assertTrue(all(holds(c, r[c.at], v) == yes for c, v, yes in conds))

  def test_say_reads_like_a_rule(self):
    d = data(); conds, _ = rules(Tree(d, d.rows))[0]
    self.assertRegex(say(conds[0]), r"(<=|>|==|!=)")
