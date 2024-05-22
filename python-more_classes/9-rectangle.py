#!/usr/bin/python3
"""Module to define a Rectangle class."""


class Rectangle:
    """Class that defines a rectangle."""

    # Public class attributes
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height  # Set height before width
        self.width = width
        # Increment the count of instances
        Rectangle.number_of_instances += 1

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
        """Return the string representation of the rectangle using the
         character(s) stored in print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = []
        for _ in range(self.__height):
            rectangle_str.append(str(self.print_symbol) * self.__width)
        return "\n".join(rectangle_str)

    def __repr__(self):
        """Return a string representation of the rectangle to
         recreate a new instance."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted
         and decrement the instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle based on the area or rect_1 if both have
         the same area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(Rectangle, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return Rectangle(size, size)
