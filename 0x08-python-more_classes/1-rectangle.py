#!/usr/bin/python3
"""Defines a real rectangle"""


class Rectangle:

    """A class that defines a rectangle with width and height"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Fetches the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with error checking"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Fetch the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with error checking"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

