#!/usr/bin/python3
"""Geometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Method initializes an instance of a Rectangle object
        Args:
            width (int): Width of the Rectangle object
            height (int): Height of the Rectangle object

        """
        self.integer_validator("width", height)
        self.__width = width
        self.integer_validator("height", width)
        self.__height = height
