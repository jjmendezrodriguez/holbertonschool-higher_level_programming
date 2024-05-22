#!/usr/bin/python3
"""Module to define a Rectangle class."""


class Rectangle:
    """Class that defines a rectangle."""

    def __init__(self, width=0, height=0):
        self.height = height  # Set height before width
        self.width = width

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle, with checks for type and value."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle, with checks for type and value."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.
        Returns 0 if either the width or the height is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the string representation of the rectangle using
         the '#' character."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = []
        for _ in range(self.__height):
            rectangle_str.append('#' * self.__width)
        return "\n".join(rectangle_str)

    def __repr__(self):
        """Return a string representation of the rectangle to
         recreate a new instance."""
        return f"Rectangle({self.__width}, {self.__height})"
