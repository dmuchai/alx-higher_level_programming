#!/usr/bin/python3
"""appends string at end of text file and returns number of characters added.
"""


def append_write(filename="", text=""):
    """Appends string at the end of text file and returns the num of charadded
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
