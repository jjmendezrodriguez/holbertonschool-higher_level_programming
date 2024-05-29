#!/usr/bin/python3
import csv
import json
"""This module provides a function to convert CSV data to
JSON format."""


def convert_csv_to_json(csv_filename):
    """
    Convert data from a CSV file to a JSON file.

    Parameters:
    csv_filename (str): The name of the CSV file to be
    converted.

    Returns:
    bool: True if the conversion was successful,
    False otherwise.
    """
    try:
        # Read the CSV file
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        # Write the JSON file
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        print(f"The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
