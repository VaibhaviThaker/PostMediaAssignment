import re
import sys
import os


class CustomCounter:
    """
        CustomCounter class defines methods that performs the following operations on a given content as a string:
        1. counts the total number of words
        2. retrieves the n most common words
    """
    def __init__(self):
        self.__count = {}

    def add_word(self, word):
        """
            method used to record the word and its occurrences
            :param word: string - each word in a line
            execution: if the word exists in the dictionary, it increments the occurrence by 1, else adds the word in the
            dictionary with occurrence value of 1
        """
        if str(word) in self.__count:
            self.__count[str(word)] += 1
        else:
            self.__count[str(word)] = 1

    def add_content(self, content):
        """
            method used to retrieve the content and add the words to the dictionary that matches the regular expression
        :param content: string - content
        """
        for w in re.findall(r'\w+', content):
            self.add_word(w)

    def most_common(self, number):
        """
            method to convert the dictionary to list and reverse it to get the n most common words in descending order
        :param number: integer - parameter determines the n most common words that needs to be returned
        :return: dictionary with n most common words and the occurrence of each word
        """
        sorted_dict = CustomCounter.__reverse_sort_dict(self.__count)
        return {k: sorted_dict[k] for k in list(sorted_dict)[:number]}

    def get_number_of_words(self):
        """
            method to return the total number of words in the string
        :return: integer - total number of words
        """
        return sum(self.__count.values())

    @staticmethod
    def __reverse_sort_dict(input_dict):
        """
            method used to convert the dictionary to list in a reverse order based on the lambda function
        :param input_dict: dictionary - the dictionary that needs to be reversed
        :return: dictionary
        """
        return {k: v for k, v in sorted(input_dict.items(), reverse=True, key=lambda item: item[1])}


def read_file(file_path):
    """
    opens the file in read mode to read UTF-8 encoded plain text file and returns the content
    :param file_path: os.path.abspath - path of the file
    :return: string - contents of the file
    """
    with open(file_path, 'r', encoding="utf-8") as content_file:
        return_value = content_file.read()
    return return_value


# main
file_content = ''
try:
    file_content = read_file(os.path.abspath(sys.argv[1]))
    custom_counter = CustomCounter()
    custom_counter.add_content(file_content)
    number_of_words = custom_counter.get_number_of_words()
    print("Number of words: " + str(number_of_words))
    print("Ten most common words and number of occurrences for each :")
    print(custom_counter.most_common(10))
except FileNotFoundError:
    print("Wrong file or file path")
except Exception as error_message:
    print("something went wrong: %s" % str(error_message))
