import unittest
from test_math_funcition import *


if __name__ == '__main__':
    suite = unittest.TestSuite()

# 用addTest()方法添加单个testcase
    suite.addTest(TestMathFunction("test_add"))

# 用addTests + TestLoader
# loadTestsFromName()，传入'模块名.TestCase名'
    suite.addTests(unittest.TestLoader().loadTestsFromName("test_math_funcition.TestMathFuncition"))

# loadTestsFromTestCase()，传入TestCase
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunction))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
