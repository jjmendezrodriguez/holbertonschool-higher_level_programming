#!/usr/bin/python3
"""Module to define a Square class."""


class Square:
    """Class that defines a square with a
    private attribute size that must be an integer and non-negative."""

    def __init__(self, size=0):
        """Initialize a new Square with a given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
