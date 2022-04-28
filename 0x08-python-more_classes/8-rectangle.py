#!/usr/bin/python3
"""
Represents a rectangle class
"""


class Rectangle:
    """
    A rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes an instance of a rectangle object
        Args:
            width (int): width of rectangle
            height (int): height of a rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        ret = []
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            ret.append(str(self.print_symbol) * self.__width)
        return "\n".join(ret)
    
    def __repr__(self):
        """
        Method a string representation of the rectangle
            to be able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
    
    def __del__(self):
        """
        deletes an instance of Rectangle object
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        compares the area of  two instances of the Rectangle object
        Args:
            rect_1 (Rectangle): Rectangle object instance 1
            rect_2 (Rectangle): Rectangle object instance 2
        Returns: The larger object instance in terms of area
                 or rect_1 if both are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        return rect_2
