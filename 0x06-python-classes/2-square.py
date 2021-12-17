#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Represents a Square class"""

    def __init__(self, size=0):
        """Initializes a new class
        Args:
            size (int): size of square
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
