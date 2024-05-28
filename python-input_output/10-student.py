#!/usr/bin/python3
"""Module defining the Student class and its methods."""


class Student:
    """
    Defines a student with first name, last name, and age attributes.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve.
                                     If None, all attributes will be retrieved.

        Returns:
            dict: A dictionary containing specified attributes of
            the Student instance.
        """
        if isinstance(
                attrs, list) and all(isinstance(item, str) for item in attrs):
            """Return only the specified attributes in attrs if all
            items in attrs are strings"""
            return {
                key: getattr(self, key) for key in attrs if hasattr(self, key)}
        else:
            # Return all attributes if attrs is not a list of strings
            return self.__dict__
