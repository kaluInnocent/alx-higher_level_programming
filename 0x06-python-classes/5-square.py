#!/usr/bin/python3
"""A Square class"""


class Square:
    """Defines a Square class"""

    def __init__(self, size=0):
        """Initializes a Square object
        Args:
            size (int): size of a square
        """
        self.__size = size

    @property
    def size(self):
        """A getter method that retrieves data"""
        return self.__size

    @size.setter
    def size(self, value):
        """A setter method that sets the value of a size
        Args:
            value (int): user defined value
        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """computes the area of a square object"""
        return self.__size ** 2

    def my_print(self):
        """prints '#' in place of area of a square """
        if self.__size > 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print("\n")
