#!/usr/bin/python3
"""Module to define a Square class."""


class Square:
    """Class that defines a square with private attribute size."""

    def __init__(self, size):
        """Initialize a new Square with a given size.

        Args:
            size (any): The size of the square, no type/value verification.
        """
        self.__size = size
