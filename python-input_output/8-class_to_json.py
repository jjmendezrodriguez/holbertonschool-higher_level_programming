#!/usr/bin/python3
"""Module to serialize class instances to JSON-compatible dictionary."""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        A dictionary containing all attributes of obj that are serializable.
    """

    """Create a dictionary comprehension that goes through each attribute
    of the object's __dict__ (which stores all its attributes).
    We only include attributes that are of
    type list, dict, str, int, or bool."""
    return {key: value for key, value in obj.__dict__.items()
            if type(value) in [list, dict, str, int, bool]}
