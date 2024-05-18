#!/usr/bin/python3
"""Module to define a Square class."""


class Square:
    """Class that defines a square with private attributes
    'size' and 'position'."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with a given size and position

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.
            Defaults to (0, 0)."""

        self.size = size  # This uses the size setter
        self.__position = position  # This uses the position setter

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
        if (isinstance(value, tuple)):
            if all(isinstance(num, int) for num in value) and (
                 all(num >= 0 for num in value)) and len(value) == 2:
                self.__position = value
            else:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")

    def area(self):
        """Calculate and return the area of the square.

        Returns:
           int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#' using
        the position attribute."""
        if self.size > 0:
            for _ in range(self.position[1]):
                print("")  # Print an empty line if size is 0
            for count, _ in enumerate(range(self.size)):
                for _ in range(self.position[0]):
                    print(" ", end="")
                for _ in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
