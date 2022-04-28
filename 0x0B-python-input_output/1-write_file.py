#!/usr/bin/python3
"""Function writes to a file"""


def write_file(filename="", text=""):
    """
     Function writes a string to a text file and returns
     the number of characters written
     Args:
         filename: file to be written into
         text: text to be written
     Returns: (int) The number of count of characters written into filename

    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(str(text))
