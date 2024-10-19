#!/usr/bin/python3
"""a function that returns the JSON representation of a Python object"""


import json


def to_json_string(my_obj):
    """Writes a Python object to a JSON file."""
    return json.dumps(my_obj)
