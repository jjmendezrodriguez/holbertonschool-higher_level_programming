#!/usr/bin/python3
"""Print a Triangle"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        List[List[int]]: A list of lists of integers
        representing the Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # The first row is always [1].

    for i in range(1, n):
        row = [1]  # Every row starts with 1.
        last_row = triangle[-1]
        for j in range(1, i):
            # Each element is the sum of the two elements above it.
            row.append(last_row[j - 1] + last_row[j])
        row.append(1)  # Every row ends with 1.
        triangle.append(row)

    return triangle
