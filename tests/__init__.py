import unittest

import tests.zip_processor_test as zpt
import tests.shell_processor_test as spt

if __name__ == '__main__':
    suites = unittest.TestSuite()
    suites.addTest(zpt.ZipProcessorTester('test_execute'))
    suites.addTest(spt.ShellProcessorTest('test_shell_cmd_execute'))

    unittest.TextTestRunner().run(suites)