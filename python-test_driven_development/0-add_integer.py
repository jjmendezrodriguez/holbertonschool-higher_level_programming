#!/usr/bin/python3
"""
This module define
    Prototype:
        def add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after converting them to integers.

    Args:
    a (int, float): The first number to add. Must be an integer or float,
     otherwise a TypeError is raised.
    b (int, float, optional): The second number to add. Defaults to 98.
    Must be an integer or float, otherwise a TypeError is raised.

    Returns:
    int: The sum of a and b after both have been converted to integers.

    Raises:
    TypeError: If either a or b is neither an integer nor a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
