#!/usr/bin/python3
"""module: json representation of an object """
import json


def to_json_string(my_obj):
    """
    Function returns the json representation of an object
    Args:
        my_obj: object whose json is to be returned
    Returns: A json rep of the object

    """
    return json.dumps(my_obj)
