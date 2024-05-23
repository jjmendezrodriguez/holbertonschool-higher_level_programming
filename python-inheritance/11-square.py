#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square is a subclass of Rectangle.

    It is initialized with size, which must be a positive integer.
    """

    def __init__(self, size):
        """
        Initializes a Square with size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string describing the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
