import unittest
import three

class Test(unittest.TestCase):

  def test_string_to_list(self):
    self.assertEqual(three.string_to_list('''R1,L2
L3,U4'''), [['R1', 'L2'], ['L3', 'U4']])

  def test_create_points_list(self):
    self.assertEqual(three.create_points_list([['R1', 'L2'], ['L3', 'U2']]),
    [[(1, 0), (0, 0), (-1, 0)], [(-1, 0), (-2, 0), (-3, 0), (-3, 1), (-3, 2)]])

  def test_matching_points_list(self):
    self.assertEqual(three.matching_points_list([[(0, 4), (2, 5)], [(2, 5), (6, -3)]]), [(2, 5)])

  def test_compute_answer(self):
    self.assertEqual(three.compute_answer('''R1,U2,R1
U1,R2,U1'''), (2, 4))

unittest.main()