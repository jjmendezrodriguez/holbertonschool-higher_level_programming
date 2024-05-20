#!/usr/bin/python3
""" 
This module define
    Prototype:
        def matrix_divided(matrix, div):
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and returns a
    new matrix with the results rounded to 2 decimal places.

    Args:
    matrix (list of lists of int/float): The matrix to be divided.
    div (int/float): The divisor by which matrix elements will be divided.

    Raises:
    TypeError: If the matrix is not a list of lists of integers/floats,
     or if each row of the matrix does not have the same size.
    TypeError: If div is not a number.
    ZeroDivisionError: If div is zero.

    Returns:
    list: A new matrix with all elements divided by div and rounded to
     2 decimal places.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix) or not all(
             isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
