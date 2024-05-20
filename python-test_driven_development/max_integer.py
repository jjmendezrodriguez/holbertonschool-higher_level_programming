#!/usr/bin/python3
def max_integer(list=[]):
    """Returns the maximum integer from a list of integers."""
    if not list:
        return None
    max_val = list[0]
    for num in list:
        if num > max_val:
            max_val = num
    return max_val
