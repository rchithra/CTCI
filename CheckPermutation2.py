"""
Given two strings, write a method to decide if one is a permutation of the other.
"""
from collections import Counter
import unittest


def checkPermutations(string1, string2):
    if len(string1) != len(string2):
        return False
    counter = Counter()
    for i in string1:
        counter[i] += 1
    for i in string2:
        if counter[i] == 0:
            return False
        counter[i] -= 1

    return True


class Test(unittest.TestCase):
    dataTrue = (('abcd', 'bacd'), ('325676', '567632'), ('fer23f', 'ref3f2'))
    dataFalse = (('abcd', 'd2cba'), ('2345', '6789'), ('sdf23', 'sdf43'))

    def test_checkPermutation(self):
        for test in self.dataTrue:
            result = checkPermutations(*test)
            self.assertTrue(result)
        for test in self.dataFalse:
            result = checkPermutations(*test)
            self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
