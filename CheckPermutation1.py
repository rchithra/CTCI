"""
Given two strings, write a method to decide if one is a permutation of the other.
"""
import unittest


def checkPermutation(string1, string2):
    if len(string1) != len(string2):
        return False
    a = sorted(string1)
    b = sorted(string2)
    for i in range(0, len(string1)):
        if a[i] != b[i]:
            return False
    return True


if __name__ == '__main__':
    string1 = "test"
    string2 = "wtet"

    if checkPermutation(string1, string2):
        print("Yes")
    else:
        print("No")
