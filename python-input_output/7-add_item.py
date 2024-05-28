#!/usr/bin/python3
"""Script to add command-line arguments to a list and save them to a JSON file."""

import sys
from 5_save_to_json_file import save_to_json_file
from 6_load_from_json_file import load_from_json_file

# The filename where the data will be saved
filename = "add_item.json"

try:
    # Try to load the existing data from the file
    items = load_from_json_file(filename)
except (FileNotFoundError, json.JSONDecodeError):
    # If the file doesn't exist or contains invalid JSON, start with an empty list
    items = []

# Extend the list with the arguments provided on the command line (excluding the script name)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
