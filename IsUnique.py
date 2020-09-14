"""
Implement an algorithm to determine if a string has all unique characters .
What if yoy cannot use additional data structures ?
"""
import unittest


def is_unique(string):
    if len(string) > 128:
        return False

    charset = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if charset[val]:
            return False
        charset[val] = True

    return True


class Test(unittest.TestCase):
    true_data = ['mystring', 'asdfg', 'qwerty', '2dsg53', ' ']
    false_data = ['solutions', '23gh rt2', 'newnest']

    def test_is_unique(self):
        for char in self.true_data:
            input_str = is_unique(char)
            self.assertTrue(input_str)
        for char in self.false_data:
            input_str = is_unique(char)
            self.assertFalse(input_str)


if __name__ == "__main__":
    unittest.main()
