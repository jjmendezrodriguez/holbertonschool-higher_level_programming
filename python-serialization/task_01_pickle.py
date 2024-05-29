#!/usr/bin/python3
"""
This module provides a custom class for serialization
and deserialization using the pickle module.
"""
import pickle
"""
The CustomObject class represents a simple object with
attributes name, age, and is_student.
It includes methods for displaying the object's attributes,
serializing the object to a file, and deserializing
the object from a file.
"""


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes in a readable format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance of the object and
        save it to the provided filename.

        Parameters:
        filename (str): The filename where the object will be
        saved.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"An error occurred while serializing '{filename}': {e}")

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance of the CustomObject
        from the provided filename.

        Parameters:
        filename (str): The filename from which the object
        will be loaded.

        Returns:
        CustomObject: The deserialized instance of CustomObject,
        or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                return obj
        except Exception as e:
            print(f"An error occurred while deserializing '{filename}': {e}")
            return None
