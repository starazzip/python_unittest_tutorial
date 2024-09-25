# tests/test_calculator.py
import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)
import unittest

from src.calculator import Calculator


def setUpModule():
    print("[Module] setUpModule")


def tearDownModule():
    print("[Module] tearDownModule")


class TestFixtureCalculator1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()
        print("[Class 1] setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("[Class 1] tearDownClass")

    def setUp(self):
        print("[Method 1] setUp")

    def tearDown(self):
        print("[Method 1] tearDown")

    def test_add(self):
        print("[Test 1] 测试加法")
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_divide(self):
        print("[Test 1] 测试除法")
        self.assertEqual(self.calc.divide(10, 2), 5)


class TestFixtureCalculator2(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
        print("[Method 2] setUp")

    def tearDown(self):
        print("[Method 2] tearDown")

    def test_add(self):
        print("[Test 2] 测试加法")
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_divide(self):
        print("[Test 2] 测试除法")
        self.assertEqual(self.calc.divide(10, 2), 5)


if __name__ == '__main__':
    unittest.main()
