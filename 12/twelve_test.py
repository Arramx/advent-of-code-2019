import unittest
import twelve

class Test(unittest.TestCase):
  def setUp(self):
    self.moon = twelve.Moon(5, -4, 6)
    self.rest = (twelve.Moon(1, 10, 4), twelve.Moon(5, -5, 2))

  def test_string_to_list(self):
    self.assertEqual(twelve.string_to_list('''<x=16, y=-11, z=2>
<x=0, y=-4, z=7>'''), [[16, -11, 2], [0, -4, 7]])

  def test_gravity(self):
    self.moon.gravity(self.rest)
    self.assertEqual((self.moon.dx, self.moon.dy, self.moon.dz), (-1, 0, -2))

  def test_velocity(self):
    self.moon.gravity(self.rest)
    self.moon.velocity()
    self.assertEqual((self.moon.x, self.moon.y, self.moon.z), (4, -4, 4))

  def test_energy(self):
    self.moon.gravity(self.rest)
    self.moon.velocity()
    self.assertEqual(self.moon.energy(), 36)

  def test_calculate1(self):
    self.assertEqual(twelve.calculate1('''<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>''', 10), 179)
    self.assertEqual(twelve.calculate1('''<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>''', 100), 1940)

  def test_calculate2(self):
    self.assertEqual(twelve.calculate2('''<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>'''), 2772)
    self.assertEqual(twelve.calculate2('''<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>'''), 4686774924)

unittest.main()