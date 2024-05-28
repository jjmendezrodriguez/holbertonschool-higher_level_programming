#!/usr/bin/python3
"""Module for converting Python objects to JSON strings."""

import json


def to_json_string(my_obj):
    """
    Returns the JSON string representation of a Python object.

    Args:
        my_obj: The Python object to serialize.

    Returns:
        str: JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
