import unittest
import eleven

class Test(unittest.TestCase):
  def test_string_to_dict(self):
    self.assertEqual(eleven.string_to_dict('3,225,7'), {0:3, 1:225, 2:7})

  def test_change_direction(self):
    self.assertEqual(eleven.change_direction(0, 1, 0), (-1, 0))
    self.assertEqual(eleven.change_direction(0, 1, 1), (1, 0))
    self.assertEqual(eleven.change_direction(1, 0, 1), (0, -1))
    self.assertEqual(eleven.change_direction(1, 0, 0), (0, 1))
    self.assertEqual(eleven.change_direction(-1, 0, 0), (0, -1))

unittest.main()