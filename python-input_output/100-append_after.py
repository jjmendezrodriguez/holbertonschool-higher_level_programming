#!/usr/bin/python3
"""
This module provides a function 'append_after' that inserts a
specific string into a file. It adds the string after each line
that contains a specified search string. This functionality
is useful for modifying files in a targeted way, such as adding
comments or additional data where certain patterns or keywords exist.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing
    a specific string.

    Args:
        filename (str): The path to the file.
        search_string (str): The string to search for within the
        file's content.
        new_string (str): The string to append after each line
        containing the search string.
    """
    try:
        # Attempt to open the file and read lines
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        # If the file does not exist, create an empty list of lines
        lines = []

    # Create a new list to store modified lines
    new_lines = []
    for line in lines:
        # Append the current line to the new list
        new_lines.append(line)
        # Check if the current line contains the search string
        if search_string in line:
            # If so, append the new string as a new line
            new_lines.append(new_string + '\n')

    # Write the modified or new lines back to the file
    with open(filename, 'w') as file:
        file.writelines(new_lines)
