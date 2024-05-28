#!/usr/bin/python3
"""Module to read and print a text file to stdout."""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout.

    Args:
        filename (str): The path to the file to be read.
    """
    with open(filename, 'r', encoding='UTF8') as f:
        print(f.read(), end='')
