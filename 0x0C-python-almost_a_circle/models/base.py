#!/usr/bin/python3
"""A Base class"""
import json


class Base:
    """A class representing a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method constructs an instance of the Base class
        Args:
            id (any)
        """
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a python dictionary to JSON string
        Args:
            list_dictionaries (list)
        Returns: A JSON string representation of list_dictionaries

        """
        if list_dictionaries is None or len(list_dictionaries) == 0\
                or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)
