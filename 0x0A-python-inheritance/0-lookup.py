#!/usr/bin/python3
"""
This module provides a function to return the list of available attributes
and methods of an object. It can be used to inspect the structure of an object.
"""


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    This function takes any object as an argument and uses the built-in
    `dir()` function to return a list of all attributes and methods associated
    with the given object.

    Args:
        obj (any): The object whose attributes and methods are to be returned.

    Returns:
        list: A list of strings reps the attributes and methods.
    """
    return dir(obj)
