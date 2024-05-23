#!/usr/bin/python3
"""
This module defines a function that adds a new attribute to
an object if possible.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute should be added.
        name (str): The name of the attribute to add.
        value: The value of the attribute to add.

    Raises:
        TypeError: If the object cannot have a new attribute with
        the message "can't add new attribute".
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
