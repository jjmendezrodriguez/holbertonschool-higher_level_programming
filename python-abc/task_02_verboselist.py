#!/usr/bin/python3
"""VerboseList class that extends the built-in list class to add
notification messages for append, extend, remove, and pop methods."""


class VerboseList(list):
    """A subclass of list that prints notifications on item addition
    and removal."""

    def append(self, item):
        """Add an item to the list and print a message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list by appending elements from the iterable
        and print a message."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Remove the first occurrence of an item from the list
        and print a message."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=None):
        """Remove and return an item at the given index
        (default is the last item) and print a message."""
        if index is None:
            index = -1
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
