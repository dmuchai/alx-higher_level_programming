#!/usr/bin/python3
"""
Module for finding a peak in a list of unsorted integers.
A peak is an element greater than or equal to its neighbors.
"""


def find_peak(list_of_integers):
    """
    Finds a peak element in a list of unsorted integers.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int or None: A peak element if one exists, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
