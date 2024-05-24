#!/usr/bin/python3
"""Module demonstrating multiple inheritance with Fish, Bird,
and FlyingFish classes."""


class Fish:
    """A class representing a fish."""

    def swim(self):
        """Prints a message indicating that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Prints a message indicating the habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """A class representing a bird."""

    def fly(self):
        """Prints a message indicating that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Prints a message indicating the habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish that inherits from
    both Fish and Bird."""

    def fly(self):
        """Prints a message indicating that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints a message indicating that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints a message indicating the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
