# tests/test_calculator.py
import os
import sys
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)
import unittest
from src.calculator import Calculator

def setUpModule():
    print("[Module] 在整个模块的测试开始前执行一次")

def tearDownModule():
    print("[Module] 在整个模块的测试结束后执行一次")

class TestFixtureCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()
        print("[Class] 在所有测试方法之前执行一次")

    @classmethod
    def tearDownClass(cls):
        print("[Class] 在所有测试方法之后执行一次")

    def setUp(self):
        print("[Method] 开始执行测试方法")

    def tearDown(self):
        print("[Method] 测试方法执行完毕")

    def test_add(self):
        print("[Test] 测试加法")
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_divide(self):
        print("[Test] 测试除法")
        self.assertEqual(self.calc.divide(10, 2), 5)

if __name__ == '__main__':
    unittest.main()
