#!/usr/bin/python3
def islower(c):
    for char in range(97, 123):
        if ord(c) == char:
            return True
        else:
            return False
