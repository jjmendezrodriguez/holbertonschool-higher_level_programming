#!/usr/bin/python3
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test with a list of integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        
        # Test with a list containing one element
        self.assertEqual(max_integer([1]), 1)
        
        # Test with a list containing same elements
        self.assertEqual(max_integer([7, 7, 7]), 7)
        
        # Test with an empty list
        self.assertIsNone(max_integer([]))
        
        # Test with None input
        self.assertIsNone(max_integer())
        
        # Test with a mixed list
        self.assertEqual(max_integer([-1, 100, 3, 50]), 100)
        
        # Test with a list of negative numbers
        self.assertEqual(max_integer([-10, -20, -30]), -10)

    def test_type_errors(self):
        # Test with a non-list input
        with self.assertRaises(TypeError):
            max_integer("hello")
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()
