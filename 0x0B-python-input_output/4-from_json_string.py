#!/usr/bin/python3
"""a function that returns a Python object represented by a JSON string"""


import json


def from_json_string(my_str):
    """Converts JSON strings to Python objects."""
    return json.loads(my_str)
