#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits
from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle is a subclass of BaseGeometry.

    It is initialized with width and height, both of which
    must be positive integers.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
