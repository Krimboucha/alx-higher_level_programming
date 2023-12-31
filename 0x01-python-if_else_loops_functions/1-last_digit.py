#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
sign = 1
if number < 0:
    sign = -1
last_digit = abs(number) % 10
last_digit *= sign
if last_digit > 5:
    rest = "greater than 5"
elif last_digit == 0:
    rest = "0"
else:
    rest = "less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} and is {rest}")
