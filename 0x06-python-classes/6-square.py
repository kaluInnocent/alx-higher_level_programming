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
        self.__size = size
        self.__position = position

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
        if len(value) == 2 and isinstance(value, tuple):
            for i in value:
                if isinstance(i, int) and i >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """computes the area of a square object"""
        return self.__size ** 2

    def my_print(self):
        """Prints according to the size of square"""
        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
