#!/usr/bin/python3
"""Module to define a Square class."""


class Square:
    """Class that defines a square with private attributes
     'size' and 'position'."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with a given size and position.

        Args:
            size (int, optional): The size of the square, defaults to 0.
            position (tuple, optional): The position of the square as
            a tuple of 2 positive integers, defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a
             tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        # Uses the size setter to validate and set the size
        self.position = position
        # Uses the position setter to validate and set the position

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square calculated as size squared.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#' using
         the position attribute."""
        print(self.__str__())

    def __str__(self):
        """Define the print() representation of the Square.

        Returns:
            str: Formatted string representation of the square.
        """
        if self.__size == 0:
            return ""
        result = "\n" * self.__position[1]
        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result.rstrip()
