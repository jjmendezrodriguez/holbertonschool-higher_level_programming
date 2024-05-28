#!/usr/bin/python3
"""Module for loading Python objects from a JSON file."""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The path to the JSON file to read from.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, 'r', encoding='UTF8') as f:
        return json.load(f)
