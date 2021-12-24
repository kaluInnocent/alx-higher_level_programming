#!/usr/bin/python3
"""sort list"""


class  MyList(list):
    """A class that inherits from a list object"""

    def print_sorted(self):
        """Method prints the list in sorted format (ascending sort)"""
        print(sorted(self))
