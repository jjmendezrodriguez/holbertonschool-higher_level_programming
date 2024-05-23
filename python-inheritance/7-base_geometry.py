#!/usr/bin/python3
"""
This module defines a class BaseGeometry with methods to
calculate area and validate integers.
"""


class BaseGeometry:
    """
    BaseGeometry is a class with methods area and integer_validator.
    """

    def area(self):
        """
        Raises an Exception with the message area() is not implemented.

        Raises:
            Exception: always raises with the message area()
            is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer and greater than 0.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer with the message <name>
            must be an integer.
            ValueError: If value is less than or equal to
            0 with the message <name>
            must be greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
