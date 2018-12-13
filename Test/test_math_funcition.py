import unittest
from math_function import *


class TestMathFunction(unittest.TestCase):
    # 测试math_function.py

    '''@classmethod
    def setUpClass(cls):
        print("This method only use once before the first test case")

    @classmethod
    def tearDownClass(cls):
        print("This method only use once after the last test case")

    def setUp(self):
        print("Do something before test,prepare environment.")

    def tearDown(self):
        print("Do something after test,clean up.")'''

    def test_add(self):
        print("add")
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 3))

    # 跳过，不执行这条case
    @unittest.skip("I don't want to run this case")
    def test_minus(self):
        print("minus")
        self.assertEqual(1, minus(3, 2))
        self.assertNotEqual(1, minus(2, 2))

    # 另外一种方式，跳过，不执行这条case
    def test_multi(self):
        self.skipTest("Do not run this case")
        print("multi")
        self.assertEqual(4, multi(2, 2))
        self.assertNotEqual(4, multi(2, 3))

    def test_divide(self):
        print("divide")
        self.assertEqual(2, divide(6, 3))
        self.assertNotEqual(2, divide(6, 2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
