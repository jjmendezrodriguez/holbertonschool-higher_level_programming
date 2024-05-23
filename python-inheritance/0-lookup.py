#!/usr/bin/python3
"""This module define the function lookup attribute list.

 Prototype:
    def lookup:
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing the attributes and
         methods of the object.
    """
    return dir(obj)
