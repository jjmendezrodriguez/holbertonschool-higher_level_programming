#!/usr/bin/python3
"""
This module defines the MyList class, the lookup function,
the is_same_class function,
the is_kind_of_class function, and the inherits_from function.

Classes:
    MyList: Inherits from the built-in list class and provides a
    method to print the list sorted.
Functions:
    lookup: Returns the list of available attributes and methods
    of an object.
    is_same_class: Checks if an object is exactly an instance of
    the specified class.
    is_kind_of_class: Checks if an object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class.
    inherits_from: Checks if an object is an instance of a
    class that inherited (directly or indirectly) from the specified class.
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


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of,
    or if the object is an instance of a class
    that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of or inherited from
        a_class, False otherwise.
    """
    return isinstance(obj, a_class)


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a class that inherited from
        a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
