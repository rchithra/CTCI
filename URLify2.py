"""
Write a method to replace all the spaces in a string with '%20'. You may assume that the string has sufficient space at
the end to hold the additional characters, and that you are given the true length of the string.
"""
import unittest


def urlify(string, length):
    new_index = len(string)
    print("Length of original string " + str(new_index))

    for i in reversed(range(length)):
        if string[i] == ' ':
            print("new_index is {} and string is {}:".format(new_index, string[i] ))
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            print("new_index is: {} and string is {} ".format(new_index, string[i]))
            string[new_index - 1] = string[i]
            new_index -= 1
            print(new_index)

    return string


class Test(unittest.TestCase):
    data = [
        (list('much ado about nothing      '), 22\,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)
            print(actual)


if __name__ == "__main__":
    unittest.main()
