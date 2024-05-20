#!/usr/bin/python3
"""
This module defines the function text_indentation that processes a given text,
adding two new lines after each '.', '?', and ':' character without adding
extra spaces at the beginning or end of each printed line.

Prototype:
    def text_indentation(text):
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
    text (str): The text to process. Must be a string.

    Raises:
    TypeError: If the text is not a string.

    Returns:
    None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in ".?:":
            print("\n" * 2, end='')
            i += 1  # Skip any space immediately after a delimiter
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
