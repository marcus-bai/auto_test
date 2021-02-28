import unittest
from case_api.module04.case.poetryFull import poetryFull


suite = unittest.TestSuite()
suite.addTest(poetryFull('test_poetryFull_case01'))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)