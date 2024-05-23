# 7-base_geometry.py

"""
Module for geometry-related operations.
"""

class BaseGeometry:
    """
    Base class for geometry operations.
    """
    
    def __init__(self):
        """
        Initialize the BaseGeometry class with an empty list.
        """
        self.values = []

    def area(self):
        """
        Calculate the area of a geometric shape.
        
        Raises:
            Exception: if the method is not implemented.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validate if a value is a positive integer.
        
        Args:
            name (str): The name of the value.
            value (int): The value to validate.
        
        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
    
    def append(self, value):
        """
        Append a value to the internal list after validation.
        
        Args:
            value (int): The value to append.
        
        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is less than or equal to 0.
        """
        self.integer_validator("value", value)
        self.values.append(value)
    
    def print_sorted(self):
        """
        Print the internal list in ascending order.
        """
        print(sorted(self.values))
