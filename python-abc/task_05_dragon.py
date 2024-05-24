#!/usr/bin/python3
"""Module demonstrating mixin classes with SwimMixin,
FlyMixin, and Dragon classes."""


class SwimMixin:
    """A mixin that provides swimming ability."""

    def swim(self):
        """Prints a message indicating that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """A mixin that provides flying ability."""

    def fly(self):
        """Prints a message indicating that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class representing a dragon that can both swim and fly,
    inheriting from SwimMixin and FlyMixin."""

    def roar(self):
        """Prints a message indicating that the dragon roars."""
        print("The dragon roars!")
