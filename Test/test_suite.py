import unittest
from test_math_funcition import TestMathFunction
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunction("test_add"), TestMathFunction("test_minus"), TestMathFunction("test_multi"),
             TestMathFunction("test_divide")]
    suite.addTests(tests)

    # with open('unittestTextReport.txt','a') as f:
    # runner=unittest.TextTestRunner(stream=f,
    with open('HTMLReport.html', 'w') as f:
        runner = HTMLTestRunner(stream=f,
                              title ='MathFunc Test Report',
                              description ='The just is a testing.',
                              verbosity=2)
        runner.run(suite)

    f.close()
