#!/usr/bin/python3
"""write to file with json"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function writes an object to text file using JSON representation
    Args:
        my_obj: object to be written
        filename: file where object is to be written
    Returns: returns the written file

    """
    with open(filename, mode="w") as myfile:
        json.dump(my_obj, myfile)
