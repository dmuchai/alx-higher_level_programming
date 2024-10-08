#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function"""

    def test_positive_integers(self):
        """Test with a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_integers(self):
        """Test with a list that contains negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_integers(self):
        """Test with a list that contains both positive and negative integers"""
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_single_element(self):
        """Test with a list that contains a single element"""
        self.assertEqual(max_integer([3]), 3)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_floats(self):
        """Test with a list that contains floats"""
        self.assertEqual(max_integer([1.5, 2.3, 3.9, 0.2]), 3.9)

    def test_strings(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')
        self.assertEqual(max_integer(['apple', 'banana', 'pear']), 'pear')

    def test_none(self):
        """Test with None as input"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_arguments(self):
        """Test with no arguments passed"""
        self.assertEqual(max_integer(), None)

if __name__ == '__main__':
    unittest.main()
