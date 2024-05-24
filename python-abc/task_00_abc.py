#!/usr/bin/env python3
""" This script demonstrates the use of
Abstract Base Classes (ABCs) in Python. """

from abc import ABC, abstractmethod
""" Importing necessary components from the
abc module to create abstract base classes. """


class Animal(ABC):
    """
    Animal is an abstract class that defines an abstract method called sound.
    Classes inheriting from Animal must implement this method.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by any
        class inheriting from Animal.
        """
        pass


class Dog(Animal):
    """
    Dog is a subclass of Animal that implements the sound method.
    """

    def sound(self):
        """
        Implementation of the sound method that returns the sound a dog makes.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat is a subclass of Animal that implements the sound method.
    """

    def sound(self):
        """
        Implementation of the sound method that returns the sound a cat makes.
        """
        return "Meow"
