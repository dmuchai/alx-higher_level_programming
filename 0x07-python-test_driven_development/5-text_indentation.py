#!/usr/bin/python3
"""Defines a text indentation function."""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters:'.','?' and ':'.

    Args:
        text (str): The input text to be processed.

    Raises:
        TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    index = 0
    while index < len(text):
        result += text[index]
        if text[index] in ".?:":
            result += "\n\n"
            index += 1
            while index < len(text) and text[index] == " ":
                index += 1
            continue
        index += 1
    print(result, end="")
