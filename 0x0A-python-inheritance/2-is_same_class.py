#!/usr/bin/python3
"""Check instance of object"""


def is_same_class(obj, a_class):
    """Function checks if a given object is an instance of a specific class
    Args:'
        obj (a_class): Object whose instance is to be verified
        a_class (class): The class of the given object
    Returns: True if obj is instance of a_class, False otherwise

    """
    if type(obj) is a_class:
        return True
    return False
