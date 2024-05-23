#!/usr/bin/python3
"""
Module for geometry-related operations.
"""


class BaseGeometry:
    """
    Base class for geometry operations.
    """
    def area(self):
        """
        Calculate the area of a geometric shape.
        
        Raises:
            Exception: if the method is not implemented.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validate if a value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
