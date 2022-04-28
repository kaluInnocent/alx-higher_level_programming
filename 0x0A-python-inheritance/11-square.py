#!/usr/bin/python3
"""A Square Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initializes a new instance of a Square object
        Args:
            size (int)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Method prints a representation of the square class"""
        return "[Square] {}/{}".format(self.__size, self.__size)
