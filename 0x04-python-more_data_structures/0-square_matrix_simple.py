#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = []
        for i in matrix:
            new_matrix.append(list(map(lambda j: j**2, i)))
        return new_matrix
