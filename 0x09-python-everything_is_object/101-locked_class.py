#!/usr/bin/python3
"""Defines a class LockedClass with no class or object attribute"""

class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.

    Attributes:
    first_name(string): first name
    """

    __slots__ = ['first_name']

    def __init__(self):
        """Creates instances of Locked Class"""

        self.first_name = "first_name"
