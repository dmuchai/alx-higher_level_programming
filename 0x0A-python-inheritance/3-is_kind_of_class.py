#!/usr/bin/python3
"""check if obj is instance of a class or an instance of subclass of a_class.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance or an instance of a subclass of a_class."""
    return isinstance(obj, a_class)
