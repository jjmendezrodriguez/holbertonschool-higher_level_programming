#!/usr/bin/python3
import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Defines test cases for the max_integer function, which identifies the
    maximum integer in a list.
    """

    def test_max_integer(self):
        """
        Test various list configurations to ensure correct max integer is
        returned.
        """
        # Test with a list of integers, expect the largest value
        self.assertEqual(max_integer([1, 2, 3, 4]), 4, "Should be 4")

        # Test with negative integers, expect the least negative value
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1, "Should be -1")

        # Test with one element, expect that element
        self.assertEqual(max_integer([1]), 1, "Should be 1")

        # Test with identical elements, expect that element
        self.assertEqual(max_integer([7, 7, 7]), 7, "Should be 7")

        # Test with an empty list, expect None
        self.assertIsNone(max_integer([]), "Should be None")

        # Test without arguments, uses default empty list, expect None
        self.assertIsNone(max_integer(), "Should be None")

        # Test with mixed negative and positive numbers
        self.assertEqual(max_integer([-1, 100, 3, 50]), 100, "Should be 100")

        # Test with only negative numbers
        self.assertEqual(max_integer([-10, -20, -30]), -10, "Should be -10")

    def test_type_errors(self):
        """
        Test input types to ensure TypeErrors are raised when inputs are not
        lists.
        """
        # Test with a string, which should raise a TypeError
        with self.assertRaises(
                TypeError, msg="Should raise TypeError for string input"):
            max_integer("hello")

        # Test with None, should raise TypeError because it is not iterable
        with self.assertRaises(
                TypeError, msg="Should raise TypeError for None input"):
            max_integer(None)


if __name__ == '__main__':
    unittest.main()
