import unittest
import one

class TestString(unittest.TestCase):

  def test_to_int_list(self):
    self.assertEqual(one.to_int_list('''10
10
20'''), [10, 10, 20]) 

  def test_count_fuel(self):
    self.assertEqual(one.count_fuel([12, 14]), [2, 2])
    self.assertEqual(one.count_fuel(654), 216)

  def test_calc_fuel_fuel(self):
    self.assertEqual(one.calc_fuel_fuel([654, 2]), [312, 0])

  def test_iterate_fuel(self):
    self.assertEqual(one.iterate_fuel(654), 312)

  def test_calculate(self):
    self.assertEqual(one.calculate('''12
14'''), [4, 4])
    self.assertEqual(one.calculate('1969'), [654, 966])

unittest.main()