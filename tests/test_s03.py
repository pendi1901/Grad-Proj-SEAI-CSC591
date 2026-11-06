import random, unittest
from ezl.s03_certify import same, cliffs, ks

class TestCertify(unittest.TestCase):
  def test_same_on_same(self):
    random.seed(1); xs = [random.gauss(10, 1) for _ in range(100)]
    self.assertTrue(same(xs, [x + .01 for x in xs]))

  def test_different_on_shifted(self):
    random.seed(1); xs = [random.gauss(10, 1) for _ in range(100)]
    self.assertFalse(same(xs, [x + 2 for x in xs]))

  def test_cliffs_extremes(self):
    self.assertEqual(cliffs([1, 2, 3], [4, 5, 6]), 1)
    self.assertEqual(cliffs([1, 2, 3], [1, 2, 3]), 0)
    self.assertEqual(ks([1, 2, 3], [1, 2, 3]), 0)
