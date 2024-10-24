#!/usr/bin/python3
""" Module for testing Rectangle class functionality """

import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from unittest.mock import patch


class TestRectangleClass(unittest.TestCase):
    """ Test suite for the Rectangle class """

    def setUp(self):
        """ Method executed before each test """
        Base._Base__nb_objects = 0

    def test_rectangle_initialization(self):
        """ Test initialization of Rectangle with valid inputs """
        r = Rectangle(10, 2, 1, 1, 100)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 100)

    def test_invalid_width_type(self):
        """ Test invalid width type """
        with self.assertRaises(TypeError):
            r = Rectangle("10", 2)

    def test_invalid_height_type(self):
        """ Test invalid height type """
        with self.assertRaises(TypeError):
            r = Rectangle(10, "2")

    def test_invalid_x_type(self):
        """ Test invalid x type """
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, "1")

    def test_invalid_y_type(self):
        """ Test invalid y type """
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 1, "1")

    def test_negative_width_value(self):
        """ Test negative width value """
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 2)

    def test_negative_height_value(self):
        """ Test negative height value """
        with self.assertRaises(ValueError):
            r = Rectangle(10, -2)

    def test_negative_x_value(self):
        """ Test negative x value """
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, -1)

    def test_negative_y_value(self):
        """ Test negative y value """
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, 1, -1)

    def test_area(self):
        """ Test the area method """
        r = Rectangle(10, 2)
        self.assertEqual(r.area(), 20)

    def test_display(self):
        """ Test the display method """
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), expected_output)

    def test_str_method(self):
        """ Test the __str__ method """
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")


if __name__ == "__main__":
    unittest.main()
