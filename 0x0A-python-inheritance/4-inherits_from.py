#!/usr/bin/python3
"""checks if the object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """
    Return True if obj is instance of class that inherited from a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
