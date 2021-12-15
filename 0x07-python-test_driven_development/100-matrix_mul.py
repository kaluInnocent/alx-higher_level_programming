#!/usr/bin/python3
"""module for matrix multiplication"""


def matrix_mul(m_a, m_b):
    """
    function multiplies two matrices
    Args:
        m_a (list): first matrix
        m_b (list): second matrix
    Returns:
        result (list): A new matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if m_a == [] or m_a == [[]] or len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]] or len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        if len(row) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    result = []
    mul = 0
    for i in range(len(m_a)):
        mat = []
        for j in range(len(m_b[0])):
            for k in range(len(m_a[0])):
                mul += m_a[i][k] * m_b[k][j]
            mat.append(mul)
            mul = 0
        result.append(mat)
    return result
