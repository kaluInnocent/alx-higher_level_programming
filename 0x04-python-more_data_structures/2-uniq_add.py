#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_of_element = 0
    new_list = list(set(my_list))
    for ele in new_list:
        sum_of_element += ele
    return sum_of_element
