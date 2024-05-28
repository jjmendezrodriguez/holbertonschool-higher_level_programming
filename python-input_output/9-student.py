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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary containing all attributes of the
            Student instance.
        """
        # This could also be done by directly returning self.__dict__,
        # but we explicitly list the attributes for clarity and control.
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
