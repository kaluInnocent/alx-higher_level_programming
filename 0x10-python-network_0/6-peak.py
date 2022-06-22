#!/usr/bin/python3
"""A pick finding algorithm"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    size = len(list_of_integers)
    if size == 0 or list_of_integers == []:
        return None
    if size == 1:
        return list_of_integers[0]
    if size == 2:
        return max(list_of_integers)
    mid = size // 2
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    if peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
