#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if (abs(number) % 10) > 5:
    rest = "greater than 5"
elif (abs(number) %10 ) == 0:
    rest = "0"
else:
    rest = "less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} and is {rest}")
