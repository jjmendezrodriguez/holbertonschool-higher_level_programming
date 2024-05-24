#!/usr/bin/python3
"""A module defining the CountedIterator class,
which extends the built-in iterator to count the
number of items iterated over."""

class CountedIterator:
    """A custom iterator that keeps track of the
    number of items iterated over."""

    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable and a counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        """Return the iterator object (self)."""
        return self

    def __next__(self):
        """Fetch the next item and increment the counter.
        Raise StopIteration when done."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Return the number of items that have been iterated over."""
        return self.counter
