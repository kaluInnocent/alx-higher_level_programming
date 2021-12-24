#!/usr/bin/python3
"""check for subclass"""


def inherits_from(obj, a_class):
    """Function checks if the object is an instance of a class that inherited
     (directly or indirectly from the specified class
     Args:
         obj:
         a_class
     Returns: True if obj is an instance of an inherited class, False otherwise

     """
    return not type(obj) is a_class and issubclass(type(obj), a_class)
