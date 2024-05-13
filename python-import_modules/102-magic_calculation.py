#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):  # The loop runs from 4 to 5, inclusive.
            c = add(c, i)
        return c
    else:
        return sub(a, b)
