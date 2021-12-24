#!/usr/bin/python3
"""Represents a student class"""


class Student:
    """defines a student class object"""

    def __init__(self, first_name, last_name, age):
        """Method initializes an instance of a student object
        Args:
            first_name (str): first name of student
            last_name (str): student's last name
            age (int):  A students age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a student instance
        Returns: A dictionary object
        """
        return self.__dict__
