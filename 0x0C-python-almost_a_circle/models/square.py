#!/usr/bin/python3
"""A Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class that Rectangles"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes an instance of a Square class
        Args:
            size (int)
            x (int)
            y (int)
            id (int)

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets the value of size
        """
        return self.width

    @size.setter
    def size(self, size):
        """sets the value of width"""
        self.width = size
        self.height = size

    def __str__(self):
        """Method prints a string representation of the Square object"""
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width)
