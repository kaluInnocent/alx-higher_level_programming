#!/usr/bin/python
def no_c(my_string):
    new_str = ""
    for char in my_string:
        if char in "cC":
            continue
        else:
            new_str += char
    return new_str
