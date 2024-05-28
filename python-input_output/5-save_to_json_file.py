#!/usr/bin/python3
"""Module for saving Python objects to a file in JSON format."""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The path to the file where the
        JSON representation should be saved.

    """
    with open(filename, 'w', encoding='UTF8') as f:
        json.dump(my_obj, f)
