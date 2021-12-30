#!/usr/bin/python3
"""A Rectangle class"""
from models.base import Base


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
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Method gets the width attribute
        return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method sets the value for width
        Args:
            value (int)
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Method gets the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method sets the height attribute
        Args:
            value (int)
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Method gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value as x
        Args:
            value (int)
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Method gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y
        Args:
            value (int)
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method returns the area of a Rectangle object"""
        return self.__width * self.__height

    def display(self):
        """Method prints in stdout the Rectangle
         instance with the character #
         """
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            if i != self.__height - 1:
                print()
