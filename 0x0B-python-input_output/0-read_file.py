#!/usr/bin/python3
""" Reading a text file"""


def read_file(filename=""):
    """function reads a text file and prints it to stdout
    Args:
        filename (str): The text file to be read
    Returns: Nothing
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read())
    file.close
