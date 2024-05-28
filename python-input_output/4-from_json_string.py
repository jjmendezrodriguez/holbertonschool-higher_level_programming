#!/usr/bin/python3
"""Module for converting JSON strings to Python objects."""

import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str (str): A string representing a JSON object.

    Returns:
        object: Python object decoded from JSON string.
    """
    return json.loads(my_str)
