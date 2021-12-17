#!/usr/bin/python3
"""function divides each elements of multi-dimentional array by div"""


def matrix_divided(matrix, div):
    """function divides all elements of a matrix by div
    Args:
        matrix: list of list of (int)
        div (int) or (float): The divisor
    Returns: A new matrix containing the divided elements of the supplied matrix
    """
    if div != 0:
        if isinstance(div, int) or isinstance(div, float):
            pass
        else:
            raise TypeError("div must be a number")
    else:
        raise ZeroDivisionError("division by zero")
    if isinstance(matrix, list) and len(matrix):
        for row in matrix:
            if isinstance(row, list) and len(row):
                if len(matrix[0]) == len(row):
                    for j in row:
                        if isinstance(j, int) or isinstance(j, float):
                            pass
                        else:
                            raise TypeError("matrix must be a matrix"
                                            " (list of lists) of"
                                            " integers/floats")
                else:
                    raise TypeError("Each row of the matrix"
                                    " must have the same size")
            else:
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
    else:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]
    return new_matrix
