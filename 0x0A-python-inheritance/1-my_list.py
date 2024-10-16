#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
It includes a method to print the list in sorted order.
"""


class MyList(list):
    """
    A subclass of list with an method to print the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.

        This method simply prints a sorted version of the list.
        """
        print(sorted(self))
