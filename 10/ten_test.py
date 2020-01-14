import unittest
import ten
from collections import defaultdict

class Test(unittest.TestCase):

  def test_string_to_grid(self):
    self.assertEqual(ten.string_to_grid('''.#.#..#
##..#..'''), [['.', '#', '.', '#', '.', '.', '#'], ['#', '#', '.', '.', '#', '.', '.']])

  def test_get_asteroids_coords(self):
    self.assertListEqual(ten.get_asteroids_coords([['.', '#', '#'], ['#', '#', '.']]), [(1, 0), (2, 0), (0, 1), (1, 1)])

  def test_count_detectable(self):
    self.assertEqual(ten.count_detectable([(1, 0), (4, 0), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (4, 3), (3, 4), (4, 4)], (1, 0)), 7)

  def test_calculate1(self):
    self.assertEqual(ten.calculate1('''.#..#
.....
#####
....#
...##''', False), 8)
    self.assertEqual(ten.calculate1('''.#..#
.....
#####
....#
...##''', True), (3, 4))

  def test_calculate2(self):
    self.assertEqual(ten.calculate2('''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##'''), 802)

unittest.main()