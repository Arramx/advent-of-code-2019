import unittest
import nine

class Test(unittest.TestCase):
  def test_string_to_dict(self):
    self.assertEqual(nine.string_to_dict('3,225,7'), {0:3, 1:225, 2:7})

  def test_calculate(self):
    self.assertEqual(nine.calculate('104,1125899906842624,99', 1), 1125899906842624)
    self.assertEqual(nine.calculate('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99', 1), 99)
    self.assertTrue(len(str(nine.calculate('1102,34915192,34915192,7,4,7,99,0', 1))) == 16)

unittest.main()