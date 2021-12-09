#!/usr/bin/python3
"""A square class"""


class Square:
    """Represents a Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Method initializes an instance of a square object
        Args:
            size (int): size of a side of the square
            position (tuple): Position of space
        """
        self.size = size
        self.position = position

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
        self.__size = value

    @property
    def position(self):
        """a getter method to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """A setter method to set position to value
        Args:
            value (tuple): A tuple object
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
            not all(isinstance(i, int) for i in value)\
                or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """computes the area of a square object"""
        return self.__size ** 2

    def my_print(self):
        """Prints according to the size of square"""
        if self.__size == 0:
            print("")
            return
        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print("")
