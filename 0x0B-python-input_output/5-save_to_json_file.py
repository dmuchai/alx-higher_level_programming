#!/usr/bin/python3
"""A function that writes a Python Object to a JSON file"""


import json


def save_to_json_file(my_obj, filename):
    """Writes a Python object to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
