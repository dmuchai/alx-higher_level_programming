#!/usr/bin/python3
"""Function that that prints a certain first name and last name."""


def say_my_name(first_name, last_name=""):
    """Prints a string with <first_name> and <last_name>..

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
