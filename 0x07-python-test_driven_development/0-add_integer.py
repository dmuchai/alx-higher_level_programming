#!/usr/bin/python3
"""
This is the addition module.
it adds 2 integers a and b must be first casted
returns integer sum
"""


def add_integer(a, b=98):
    """
    Returns the addition of two integers a and b.

    Raises:
        TypeError: If either of a or b is a not an integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
