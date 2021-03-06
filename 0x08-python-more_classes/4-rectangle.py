#!/usr/bin/python3
"""
Represents a rectangle class
"""


class Rectangle:
    """
    A rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Initializes an instance of a rectangle object
        Args:
            width (int): width of rectangle
            height (int): height of a rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Method retrieves the value of width
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        A method that sets value to width
        Args:
            value (int): The value of the width of the rectangle object
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        
        self.__width = value
    
    @property
    def height(self):
        """
        A getter method that retrieves the height of the rectangle
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        A method that sets the value of the height of a rectangle
        Args:
            value (int): height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """
        Method computes the area of a rectangle object
        """
        return self.__width * self.__height
    
    def perimeter(self):
        """
        Method computes the perimeter of a rectangle object
        """
        if self.width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
    
    def __str__(self):
        """
        A method that prints the rectangle object when str is called
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            if i != self.__height - 1:
                print("")
        return ""
    
    def __repr__(self):
        """
        Method a string representation of the rectangle
            to be able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
