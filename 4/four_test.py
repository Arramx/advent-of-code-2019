import unittest
import four

class Test(unittest.TestCase):

  def test_adjacent_digits(self):
    self.assertTrue(four.adjacent_digits(777265))
    self.assertFalse(four.adjacent_digits(123456))

  def test_two_adjacent_digits(self):
    self.assertTrue(four.two_adjacent_digits(771865))
    self.assertFalse(four.two_adjacent_digits(177765))

  def test_never_decrease(self):
    self.assertTrue(four.never_decrease(123456))
    self.assertFalse(four.never_decrease(123452))

unittest.main()