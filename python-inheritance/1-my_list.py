#!/usr/bin/python3
"""
This module defines the MyList class and the lookup function.

Classes:
    MyList: Inherits from the built-in list class and provides
     a method to print the list sorted.
Functions:
    lookup: Returns the list of available attributes and methods of an object.
"""


class MyList(list):
    """
    MyList is a subclass of the built-in list class.

    Methods:
        print_sorted(self): Prints the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.

        Assumes all elements in the list are integers.
        """
        print(sorted(self))


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing the attributes and
         methods of the object.
    """
    return dir(obj)
