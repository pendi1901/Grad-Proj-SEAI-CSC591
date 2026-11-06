import unittest
from ezl.core import Num, Sym, adds, cluster
from _data import data

class TestRemember(unittest.TestCase):
  def test_num_add_then_forget(self):
    n = adds([1, 2, 3, 4, 10]); n.add(10, -1)
    self.assertAlmostEqual(n.mu, 2.5); self.assertAlmostEqual(n.div(), adds([1, 2, 3, 4]).div())

  def test_sym_entropy(self):
    self.assertAlmostEqual(adds("aabb", Sym()).div(), 1.0)

  def test_roles_and_distances(self):
    d = data()
    self.assertEqual([c.name for c in d.y], ["Cost-", "Score-", "Idle-"])
    a, b = d.rows[:2]
    self.assertEqual(d.distx(a, a), 0)
    self.assertTrue(0 <= d.distx(a, b) <= 1 and 0 <= d.disty(a) <= 1)

  def test_clusters_cover_every_row(self):
    d = data(); leaves = cluster(d)
    self.assertGreater(len(leaves), 1)
    self.assertEqual(sum(map(len, leaves)), len(d.rows))

  def test_best_cluster_beats_average(self):
    d = data(); mu = lambda rows: sum(map(d.disty, rows)) / len(rows)
    self.assertLess(min(map(mu, cluster(d))), mu(d.rows))
