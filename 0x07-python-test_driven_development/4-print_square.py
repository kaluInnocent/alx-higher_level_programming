#!/usr/bin/python3
"""Function prints a square"""


def print_square(size):
    """Function prints # in place of the area of  a square of size
    Args:
        size (int): size of the square to be printed
    Returns: Nothing
    """
    if isinstance(size, int):
        if size >= 0:
            for i in range(size):
                for j in range(size):
                    if size == 0:
                        print("")
                    else:
                        print("#", end="")
                print("")
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")
