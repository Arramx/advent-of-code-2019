import unittest
import eight
import numpy as np

class Test(unittest.TestCase):
  def test_string_to_layer_grid(self):
    self.assertTrue(np.array_equal(eight.string_to_layer_grid('875346298156', 2, 2), np.array([[[8, 7], [5, 3]], [[4, 6], [2, 9]], [[8, 1], [5, 6]]])))

  def test_find_fewest_zeros(self):
    self.assertEqual(eight.find_fewest_zeros([[[0, 7], [0, 0]], [[0, 0], [0, 0]], [[8, 1], [5, 6]]]), 2)

  def test_calculate_product(self):
    self.assertEqual(eight.calculate_product([[0, 1, 1], [0, 2, 2]]), 4)

  def test_decode(self):
    self.assertTrue(np.array_equal(eight.decode('0222112222120000', 2, 2), [[0, 1], [1, 0]]))

unittest.main()