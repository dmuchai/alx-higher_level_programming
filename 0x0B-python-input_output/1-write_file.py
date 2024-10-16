#!/usr/bin/python3
"""Writes string to text file and returns the number of characters written"""


def write_file(filename="", text=""):
    """Writes string to text file and returns the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
