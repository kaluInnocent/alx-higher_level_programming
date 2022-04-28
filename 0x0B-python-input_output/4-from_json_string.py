#!/usr/bin/python3
"""json operations"""
import json


def from_json_string(my_str):
    """
    Function returns an object represented by a JSON string
    Args:
        my_str: JSON strinmg
    Returns: A python data structure

    """
    return json.loads(my_str)
