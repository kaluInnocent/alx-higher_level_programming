#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	if matrix:
		new_mat = []
		for i in matrix:
			new_mat.append(list(map(lambda j: j**2, i)))
		return new_mat
