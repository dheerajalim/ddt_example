import unittest
from xmlrunner import xmlrunner

from ddtexample import testddt


search_tests = unittest.TestLoader().loadTestsFromTestCase(testddt)


test_suite = unittest.TestSuite([search_tests])

xmlrunner.XMLTestRunner(verbosity = 2, output='test-reports').run(test_suite)



