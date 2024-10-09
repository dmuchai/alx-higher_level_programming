#!/usr/bin/python3
"""Defines the area and perimeter of rectangle"""


class Rectangle:

    """A class that defines a rectangle's area and perimeter"""

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

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of a rectangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])
    def __repr__(self):
        """Return a string representation of the rectangle to recreate it using eval"""
        return f"Rectangle({self.__width}, {self.__height})"
