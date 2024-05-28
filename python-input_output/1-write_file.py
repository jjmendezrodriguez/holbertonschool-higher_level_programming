#!/usr/bin/python3
"""Module for writing a string to a text file and
returning the number of characters written."""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the
    number of characters written.

    Args:
        filename (str): The path to the file to be written.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='UTF8') as f:
        return f.write(text)
