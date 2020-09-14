"""
Write a method to replace all the spaces in a string with '%20'. You may assume that the string has sufficient space at
the end to hold the additional characters, and that you are given the true length of the string.
"""
import unittest

def urlify(string, length):
    return string[:length].replace(' ', '%20')


ff = urlify('much%20ado%20about%20nothing        ', 22)
print(ff)

"""
class Test(unittest.TestCase):
    data = []

    def test_urlify(self):
        for []
"""