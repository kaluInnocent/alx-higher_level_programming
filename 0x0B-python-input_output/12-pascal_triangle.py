#!/usr/bin/python3
"""pascal's triangle"""


def pascal_triangle(n):
    """Function creates a list of integers representing Pascal's triangle
    Args:
        n (int) : The number whose pascal is to be returned
    Returns: A list representing pascal's triangle

    """
    if n <= 0:
        return []
    row = [[1]]
    for i in range(n-1):
        col = [1]
        for j in range(i):
            col.append(row[-1][j] + row[-1][i + 1])
        col.append(1)
        row.append(col)
    return row
