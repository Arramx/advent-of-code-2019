import unittest
import seven

class Test(unittest.TestCase):
  def test_string_to_list(self):
    self.assertEqual(seven.string_to_list('3,225,7'), [3, 225, 7])

  def test_amp(self):
    self.assertEqual(seven.amp([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0], 4, 0), 4)

  def test_calculate(self):
    self.assertEqual(seven.calculate('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'), 43210)

  def test_feedback_loop(self):
    self.assertEqual(seven.feedback_loop('3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'), 18216)

unittest.main()