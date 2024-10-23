#!/usr/bin/python3
"""Describes Class Base"""


class Base:
    """class will be the base of all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor to initialize the object.

        Args:
            id (int): The id for the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
