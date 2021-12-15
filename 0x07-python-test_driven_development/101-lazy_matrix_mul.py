#!/usr/bin/python3
"""
Module: 101-lazy_matrix_mul
Performs matrix multiplication using the Numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Function performs matrix multiplication
    Args:
        m_a: list of lists of integers or floats
        m_b: list of lists of integers or floats

    Returns: a new matrix
    """
    return numpy.matmul(m_a, m_b)
