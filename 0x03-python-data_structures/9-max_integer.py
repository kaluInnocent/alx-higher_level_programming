#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_t = my_list[0]
    for num in my_list:
        if num > max_t:
            max_t = num
    return max_t
