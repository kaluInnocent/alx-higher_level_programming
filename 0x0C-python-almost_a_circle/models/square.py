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

    def update(self, *args, **kwargs):
        """Method updates attributes
        Args:
            args (tuple)
            kwargs (dict)
        """
        if args is not None and len(args):
            for count, item in enumerate(args):
                if count == 0:
                    self.id = item
                elif count == 1:
                    self.size = item
                elif count == 2:
                    self.x = item
                elif count == 3:
                    self.y = item
        elif kwargs is not None and len(kwargs):
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Method returns a dictionary representation of a square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

    def __str__(self):
        """Method prints a string representation of the Square object"""
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width)
