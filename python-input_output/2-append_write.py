#!/usr/bin/python3
"""Module for appending a string to the end of a text file and
returning the number of characters added."""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and
    returns the number of characters added.
    If the file doesn’t exist, it creates the file.

    Args:
        filename (str): The path to the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters appended.
    """
    with open(filename, 'a', encoding='UTF8') as f:
        return f.write(text)
