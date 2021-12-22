#!/usr/bin/python3
"""operation with json module"""
import json


def load_from_json_file(filename):
    """
    function creates an object from a JSON file
    Args:
    filename: file containing a Json file
    Returns: The newly created python object

    """
    with open(filename) as myfile:
        return json.load(myfile)
