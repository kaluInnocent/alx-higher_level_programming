#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        weight = 0
        occur = 0
        for element in my_list:
            (x, y) = element
            weight += (x * y)
            occur += y
        return weight/occur if occur > 0 else 0
    return 0
