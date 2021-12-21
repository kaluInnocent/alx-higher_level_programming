#!/usr/bin/python3
""" Reading a text file"""


def read_file(filename=""):
        """
        function reads from a file
        Args:
            filename: (str) text to be read

        Returns: Nothing

        """
        with open(filename, mode="r", encoding="utf-8") as file:
            print(file.read(), end=""))
