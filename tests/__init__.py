import unittest

import tests.zip_processor_test as zpt

if __name__ == '__main__':
    suites = unittest.TestSuite()
    suites.addTest(zpt.ZipProcessorTester('test_execute'))

    unittest.TextTestRunner().run(suites)