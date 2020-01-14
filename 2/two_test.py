import unittest
import two

class Test(unittest.TestCase):

  def test_to_num_array(self):
    self.assertEqual(two.to_num_array('1,2'), [1, 2])

  def test_calculate1(self):
    self.assertEqual(two.calculate1('1, 1, 2, 0, 99, 30, 2, 4, 2, 5, 6, 5, 1'), 3)

  def test_calculate2(self):
    self.assertEqual(two.calculate2('1, 5, 6, 0, 99, 19690719, 1, 5'), 5)


unittest.main()