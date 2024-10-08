#!/usr/bin/python3
"""A class that restricts dynamic attribute creation."""


class LockedClass:
    """
    Restricts users from adding new instance attributes,
    except when the attribute is named first_name.

    Attributes:
        first_name (str): An attribute for storing a first name.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Initialize the LockedClass with a default first_name."""

        self.first_name = "first_name"
