import unittest
import five

class Test(unittest.TestCase):
  
  def test_string_to_list(self):
    self.assertEqual(five.string_to_list('3,225,7'), [3, 225, 7])

  def test_calculate1(self):
    self.assertEqual(five.calculate1('3,0,1101,5,5,0,4,0,99'), 10)

  def test_calculate2(self):
    self.assertEqual(five.calculate2('3,9,7,9,10,9,4,9,99,-1,8'), 1)

unittest.main()