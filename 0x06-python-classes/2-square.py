#!/usr/bin/python3
"""Defines an empty class Square"""


class Square:
    """a class Square that defines a square.
    """
    def __init__(self, size=0):
        """Creates new instances of square.

        Args:
            size: size of the square (1 side).
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
