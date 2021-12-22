#!/usr/bin/python3
"""Defines a Python object"""


def class_to_json(obj):
    """Creates the dictionary description with simple data
    Args:
        obj: object for serialization
    Returns: The dictionary description of simple data structure

    """
    return obj.__dict__
