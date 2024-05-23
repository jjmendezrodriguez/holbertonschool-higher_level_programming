#!/usr/bin/python3
"""
This module defines a class BaseGeometry with a
method area that raises an Exception.
"""


class BaseGeometry:
    """
    BaseGeometry is a class with a method area that
    raises an Exception.
    """

    def area(self):
        """
        Raises an Exception with the message area()
        is not implemented.

        Raises:
            Exception: always raises with the message area()
            is not implemented.
        """
        raise Exception("area() is not implemented")
