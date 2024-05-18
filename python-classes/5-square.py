#!/usr/bin/python3
"""Module to define a Square class."""


class Square:
    """Class that defines a square with a private attribute 'size'
    that must be an integer and non-negative."""

    def __init__(self, size=0):
        """Initialize a new Square with a given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size  # This will use the setter to validate

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'."""
        if self.__size == 0:
            print("")  # Print an empty line if size is 0
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
