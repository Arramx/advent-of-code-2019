import unittest
import six

class Test(unittest.TestCase):
  def test_string_to_list(self):
    self.assertEqual(six.string_to_list('''COM)B
B)C
C)D'''), [['COM', 'B'], ['B', 'C'], ['C', 'D']])

  def test_count_orbits(self):
    self.assertEqual(six.count_orbits( [['COM', 'B'], ['B', 'C'], ['C', 'D']], 'D'), 3)

#   def test_calculate1(self):
#     self.assertEqual(six.calculate1('''COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L'''), 42)

  def test_santa_distance(self):
    self.assertEqual(six.santa_distance('''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN'''), 4)

unittest.main()