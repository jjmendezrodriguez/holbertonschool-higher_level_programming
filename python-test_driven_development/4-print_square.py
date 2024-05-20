#!/usr/bin/python3
"""
This module defines the function print_square that prints a square
using the '#' character.

Prototype:
    def print_square(size):
"""


def print_square(size):
    """
    Prints a square with the character '#' based on the specified size.

    Args:
    size (int): The size length of the square's side. Must be an integer and
                non-negative.

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.

    Returns:
    None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print('#' * size)
