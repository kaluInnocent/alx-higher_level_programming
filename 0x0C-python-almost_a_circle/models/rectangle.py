#!/usr/bin/python3
"""A Rectangle class"""
from base import Base


class Rectangle(Base):
    """A rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of the Rectangle object
        Args:
            width (any)
            height (any)
            x (any)
            y (any)
            id (any)
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
