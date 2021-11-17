#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
text1 = "Last digit of {} is {} and is greater than 5"
text2 = "Last digit of {} is {} and is less than 6 and not 0"
text3 = "Last digit of {} is {} and is 0"
if last_digit > 5:
    print(text1.format(number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print(text2.format(number, last_digit))
else:
    print(text3.format(number, last_digit))
