#!/usr/bin/python3
"""function writes to a file"""


def write_file(filename="", text=""):
    """
    Function writes a string to a text file and returns
     the number of characters written
    Args:
        filename: file to be written into
        text: file to be written

    Returns: (int) The number of characters written

    """
    with open(filename, "w", encoding="utf-8") as f:
       return f.write(text)
