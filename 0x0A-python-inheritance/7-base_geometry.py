#!/usr/bin/python3
"""Geometry class"""


class BaseGeometry:
    """A class representing base geometry"""

    def area(self):
        """Method raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method validates value
        Args:
            name (str)
            value (int)

        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
