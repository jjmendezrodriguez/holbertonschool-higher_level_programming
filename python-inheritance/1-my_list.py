#!/usr/bin/python3
"""This script includes a custom MyList class that extends Python's
built-in list to provide additional functionality for printing
the elements in a sorted order."""


class MyList(list):
    def print_sorted(self):
        """Prints the list elements in ascending order."""
        sorted_list = sorted(self)
        """ Creates a new list that
         is sorted, without modifying the original list"""
        print(sorted_list)
