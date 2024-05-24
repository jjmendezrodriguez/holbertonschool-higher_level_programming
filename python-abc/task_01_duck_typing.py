#!/usr/bin/python3

from abc import ABC, abstractmethod
""" Importing necessary components from the abc module
to create abstract base classes. """


class Shape(ABC):
    """
    Shape is an abstract class that defines abstract methods for
    area and perimeter.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method that must be implemented by any class
        inheriting from Shape to calculate the area.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method that must be implemented by any class
        inheriting from Shape to calculate the perimeter.
        """
        pass


class Circle(Shape):
    """
    Circle is a subclass of Shape that implements the area
    and perimeter methods.
    """

    def __init__(self, radius):
        """
        Initialize a Circle with a specific radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        """
        import math
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate the perimeter of the circle.
        """
        import math
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle is a subclass of Shape that implements the area
    and perimeter methods.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with a specific width and height.
        """
        self.width = width
        self.height = height
        
        if width < 0 or height < 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape. This function uses duck typing
    to call the area and perimeter methods of the shape object.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
