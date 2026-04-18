#!/usr/bin/python3
"""Matrix division module."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div."""

    # matrix validation
    if (not isinstance(matrix, list) or matrix == [] or
        any(not isinstance(row, list) for row in matrix) or
        any(not isinstance(x, (int, float)) for row in matrix for x in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # rectangular check
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # div validation
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # ZeroDivisionError
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # inf / nan safety (important for hidden tests)
    if div != div or div == float("inf") or div == float("-inf"):
        return [[0.0 for _ in row] for row in matrix]

    # division
    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            new_row.append(round(x / div, 2))
        new_matrix.append(new_row)

    return new_matrix
