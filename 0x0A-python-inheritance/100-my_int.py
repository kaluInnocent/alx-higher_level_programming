#!/usr/bin/python3
"""MyInt Class"""


class MyInt(int):
    """MyInt class inherits from int class"""

    def __eq__(self, other):
        """performs equality operation
        Args:
            other (int):
        Returns: False if self is equal to other
        """
        return self.real != other

    def __ne__(self, other):
        """checks for inequality
        Args:
            other (int):
        Returns: True if self != other
        """
        return self.real == other
