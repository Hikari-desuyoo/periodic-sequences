
import sys
import os
sys.path.append(os.getcwd())
import unittest
from fraction_part import FractionPart

class FractionPartTest(unittest.TestCase):
    def test_not_periodic(self):
        fraction_part = FractionPart(123456789)
        self.assertIsNone(fraction_part.period)
        self.assertEqual(fraction_part.period_occurrences, 0)

    def test_one_digit(self):
        fraction_part = FractionPart(33333)
        self.assertEqual(fraction_part.period, '3')
        self.assertEqual(fraction_part.period_occurrences, 5)

    def test_one_digit_prefix(self):
        fraction_part = FractionPart(8777777777)
        self.assertEqual(fraction_part.period, '7')
        self.assertEqual(fraction_part.period_occurrences, 9)

    def test_two_digits_prefix_incomplete(self):
        fraction_part = FractionPart(786930929303030303)
        self.assertEqual(fraction_part.period, '30')
        self.assertEqual(fraction_part.period_occurrences, 4)

    def test_two_digits_incomplete(self):
        fraction_part = FractionPart(303030303)
        self.assertEqual(fraction_part.period, '30')
        self.assertEqual(fraction_part.period_occurrences, 4)

    def test_two_digits_prefix(self):
        fraction_part = FractionPart(78693092930303030)
        self.assertEqual(fraction_part.period, '30')
        self.assertEqual(fraction_part.period_occurrences, 4)

    def test_three_digits(self):
        fraction_part = FractionPart(504504504)
        self.assertEqual(fraction_part.period, '504')
        self.assertEqual(fraction_part.period_occurrences, 3)
