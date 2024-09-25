# tests/test_calculator.py

import os
import sys
import unittest

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)

from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        # Arrange
        calc = Calculator()

        # Action
        result1 = calc.add(2, 3)
        result2 = calc.add(-1, 1)

        # Assert
        self.assertEqual(result1, 5)
        self.assertEqual(result2, 0)

    def test_divide(self):
        # Arrange
        calc = Calculator()

        # Action
        result = calc.divide(10, 2)

        # Assert
        self.assertEqual(result, 5)

        # Action & Assert
        with self.assertRaises(ZeroDivisionError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
