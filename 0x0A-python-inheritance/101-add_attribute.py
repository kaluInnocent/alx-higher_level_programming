#!/usr/bin/python3
"""adds attribute"""


def add_attribute(obj, att, val):
    """function adds a new attribute to an object
    Args:
        obj (any): object that receives new attribute
        att (str): name of the attribute to be added
        val (any): The value of the attribute to be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, val)
