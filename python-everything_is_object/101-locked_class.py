#!/usr/bin/python3
class LockedClass:
    def __init__(self, first_name=""):
        super().__setattr__('first_name', first_name)

    def __setattr__(self, name, value):
        if name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
