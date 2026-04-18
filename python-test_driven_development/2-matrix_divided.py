#!/usr/bin/python3
"""Bu modul matrix_divided funksiyasını təqdim edir."""


def matrix_divided(matrix, div):
    """Matrisi rəqəmə bölür və 2 rəqəmə qədər yuvarlaqlaşdırır."""
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_type)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg_type)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg_type)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError(msg_size)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Diqqət: Burada div-in inf və ya nan olması problem deyil,
    # çünki Python x / inf = 0.0 qaytarır.
    return [[round(x / div, 2) for x in row] for row in matrix]
