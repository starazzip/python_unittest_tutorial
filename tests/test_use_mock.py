# tests/test_calculator.py
import os
import sys
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)
import unittest
from unittest.mock import patch

from src.calculator import Calculator

class TestMockCalculator(unittest.TestCase):
    @patch('src.calculator.requests.get')
    def test_get_exchange_rate(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = {'rates': {'USD': 1.1}}

        calc = Calculator()
        rate = calc.get_exchange_rate('EUR')
        self.assertEqual(rate, 1.1)

if __name__ == '__main__':
    unittest.main()