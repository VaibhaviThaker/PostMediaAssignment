import unittest
from unittest.mock import patch


def suite():
    """
     Added test cases to test suites that will verify the tests mentioned in the TestWordCount
     It will only run the tests that are added to the suit
    :return: TestSuite
    """
    suites = unittest.TestSuite()
    from test_case import TestWordCount
    suites.addTest(TestWordCount('test_count_words'))
    suites.addTest(TestWordCount('test_most_common_words'))
    return suites


if __name__ == '__main__':
    """
        - mocked the command line argument by applying a patch and sending the file using the patch
        - executed the test suite
    """
    fake_args = [None, 'input.txt']
    with patch('sys.argv', fake_args):
        runner = unittest.TextTestRunner()
        runner.run(suite())