#!/usr/bin/python3
"""A student class"""


class Student:
    """represents a student object class"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new instance of student class
        Args:
            first_name (str): First name
            last_name (str): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method retrieves a dictionary representation of a student instance
        Args:
            attrs: object to be retrieved
        Returns: A dictionary object
        """
        if isinstance(attrs, list):
            if all(isinstance(i, str) for i in attrs):
                return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__
