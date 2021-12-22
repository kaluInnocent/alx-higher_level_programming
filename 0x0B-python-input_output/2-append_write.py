#!/usr/bin/python3
"""module appends string"""


def append_write(filename="", text=""):
    """
    Function appends a string at the end of a text file
    Args:
        filename: file to be appended to
        text: text to be appended
    Returns: The number of characters added

    """
    with open(filename, mode="a", encoding="utf-8") as myfile:
        return myfile.write(str(text))
