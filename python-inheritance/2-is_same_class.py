#!/usr/bin/python3
"""
This module defines the MyList class, the lookup function, and the
is_same_class function.

Classes:
    MyList: Inherits from the built-in list class and provides a method to
     print the list sorted.
Functions:
    lookup: Returns the list of available attributes and methods of an object.
    is_same_class: Checks if an object is exactly an instance of the
    specified class.
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


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
