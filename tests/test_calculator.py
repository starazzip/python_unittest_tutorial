# tests/test_calculator.py

import os
import sys
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)
import unittest
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, 1), 0)

    def test_divide(self):
        calc = Calculator()
        self.assertEqual(calc.divide(10, 2), 5)

        with self.assertRaises(ZeroDivisionError):
            calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
