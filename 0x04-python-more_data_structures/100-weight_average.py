#!/usr/bin/python3
def weight_average(my_list=[]):
    add = 0
    div = 0
    for element in my_list:
        add += (element[0] * element[1])
        div += element[1]
    avg = add / div
    return avg
