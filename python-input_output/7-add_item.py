#!/usr/bin/python3
"""Script to add command-line arguments to a list and
save them to a JSON file."""

import sys
import json

# Import the functions directly
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# The filename where the data will be saved
filename = "add_item.json"

try:
    # Try to load the existing data from the file
    items = load_from_json_file(filename)
except (FileNotFoundError, json.JSONDecodeError):
    """If the file doesn't exist or contains invalid JSON,
    start with an empty list"""
    items = []

"""Extend the list with the arguments provided on the
command line (excluding the script name)"""
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
