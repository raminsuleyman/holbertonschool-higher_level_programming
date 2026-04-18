#!/usr/bin/python3
"""Matrix division module."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div."""

    # matrix check
    if (not isinstance(matrix, list) or
        any(not isinstance(row, list) for row in matrix) or
        matrix == [] or
        any(not isinstance(x, (int, float)) for row in matrix for x in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # row size check
    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # div check
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # new matrix
    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            new_row.append(round(x / div, 2))
        new_matrix.append(new_row)

    return new_matrix
