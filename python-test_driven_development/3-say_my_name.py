#!/usr/bin/python3
"""
This module defines the function say_my_name that prints the full name
by concatenating the given first and last names.

Prototype:
    def say_my_name(first_name, last_name=""):
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first_name> <last_name>' to the standard output.
    Trims any extra spaces from the names.

    Args:
    first_name (str): The first name to print.
    last_name (str, optional): The last name to print.
     Defaults to an empty string.

    Raises:
    TypeError: If either first_name or last_name is not a string.

    Returns:
    None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Strip leading and trailing spaces from first_name and last_name
    first_name = first_name.strip()
    last_name = last_name.strip()

    # Avoid adding an extra space if last_name is empty
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
