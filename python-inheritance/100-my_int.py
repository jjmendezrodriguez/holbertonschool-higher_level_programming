#!/usr/bin/python3
"""
This module defines a class MyInt that inherits from int with
inverted == and != operators.
"""


class MyInt(int):
    """
    MyInt is a subclass of int with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Overrides the == operator to invert it.

        Args:
            other: The other value to compare.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator to invert it.

        Args:
            other: The other value to compare.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
