#!/usr/bin/env python3
import json
"""This module provides functions to serialize a
Python dictionary to a JSON file and deserialize
the JSON file to recreate the Python dictionary."""


def serialize_and_save_to_file(data, filename):
    """
    Serialize the given dictionary and save it to a JSON file.

    Parameters:
    data (dict): The dictionary to serialize.
    filename (str): The filename of the output JSON file.
    If the output file already exists, it should be replaced.
    """

    with open(filename, 'w') as file:
        json.dump(data, file)
 

def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it into a dictionary.

    Parameters:
    filename (str): The filename of the input JSON file.

    Returns:
    dict: The deserialized dictionary from the JSON file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
