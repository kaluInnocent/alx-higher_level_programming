#!/usr/bin/python3
"""Checks for object instance"""


def is_kind_of_class(obj, a_class):
    """Function checks if the object is an instance of,
    or if the object is an instance of a class
     that inherited from the specified class
    Args:
        obj (a_class):
        a_class (class):
    Returns: True if obj is instance of a_class, otherwise False

     """
    return isinstance(obj, a_class)
