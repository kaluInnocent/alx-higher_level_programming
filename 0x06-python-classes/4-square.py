#!/usr/bin/python3
"""A class Square"""


class Square:
    """Represents a Square class"""

    def __init__(self, size=0):
        """Initializes an instance of the Square class
        Args:
            size (int): Size of the square
        """
        self.__size = size

    @property
    def size(self):
        """A getter method to retrieve value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set value
        Args:
            value (int): of the a side of the square
        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of Square"""
        return self.__size ** 2
