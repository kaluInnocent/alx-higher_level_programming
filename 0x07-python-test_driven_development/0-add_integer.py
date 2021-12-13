#!/usr/bin/python3
"""A function that prints a square"""


def add_integer(a, b=98):
    """Function adds two number provided they are integers
        if they are floats, they are typecasted into integers first
    Args:
        a (int): First first interger to be supplied
        b (int): second integer to be supplied
    Returns: Returns a + b
    """
    if isinstance(a, int) or isinstance(a, float):
        if isinstance(b, int) or isinstance(b, float):
            return int(a + b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
