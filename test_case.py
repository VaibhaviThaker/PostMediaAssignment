import unittest
from word_counter import CustomCounter, read_file


class TestWordCount(unittest.TestCase):

    """
        TestWordCount class is extended from python unittest.TestCase to create unit tests to verify the following:
            - total number of words
            - 10 most common words and number of occurrences for each
    """

    def setUp(self):
        self.customCounter = CustomCounter()
        self.customCounter.add_content(read_file("input.txt"))

    def test_count_words(self):
        """
            test for confirming the total number of words in a text file - input.txt
        """
        total_number_of_words = 48
        self.assertEqual(self.customCounter.get_number_of_words(), total_number_of_words, "Total number of words do not match")

    def test_most_common_words(self):
        """
            test for confirming the 10 most common words and number of occurrences for each
        """
        self.most_common_test_dict = {'Wikipedia': 5, 'and': 3, 'data': 3, 'a': 2, 'it': 2, 'from': 2, 'get': 2, 'is': 1, 'Python': 1, 'library': 1}
        self.assertDictEqual(self.customCounter.most_common(10), self.most_common_test_dict,
                             "Most common words do not match")

    def tearDown(self):
        self.customCounter = None


