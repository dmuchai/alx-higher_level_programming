#!/usr/bin/python3
""" Module for testing Square class functionality """

import unittest
from models.square import Square
from models.base import Base
from io import StringIO
from unittest.mock import patch


class TestSquareClass(unittest.TestCase):
    """ Test suite for the Square class """

    def setUp(self):
        """ Method executed before each test """
        Base._Base__nb_objects = 0

    def test_square_initialization(self):
        """ Test initialization of Square with valid inputs """
        s = Square(5, 1, 1, 100)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 1)
        self.assertEqual(s.id, 100)

    def test_invalid_size_type(self):
        """ Test invalid size type """
        with self.assertRaises(TypeError):
            s = Square("5")

    def test_negative_size_value(self):
        """ Test negative size value """
        with self.assertRaises(ValueError):
            s = Square(-5)

    def test_negative_x_value(self):
        """ Test negative x value """
        with self.assertRaises(ValueError):
            s = Square(5, -1)

    def test_negative_y_value(self):
        """ Test negative y value """
        with self.assertRaises(ValueError):
            s = Square(5, 1, -1)

    def test_area(self):
        """ Test the area method """
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        """ Test the display method """
        s = Square(2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s.display()
            self.assertEqual(str_out.getvalue(), expected_output)

    def test_str_method(self):
        """ Test the __str__ method """
        s = Square(5, 2, 3, 9)
        self.assertEqual(str(s), "[Square] (9) 2/3 - 5")


if __name__ == "__main__":
    unittest.main()
