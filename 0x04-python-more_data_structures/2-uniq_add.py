#!/usr/bin/python3
def uniq_add(my_list=[]):
	sum_ele = 0
	new = list(set(my_list))
	for element in new:
		sum_ele += element
	return sum_ele
