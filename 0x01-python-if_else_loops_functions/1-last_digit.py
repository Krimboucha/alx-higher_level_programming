#!/bin/bash/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if last_digit > 5:
    rest = "greater than 5"
elif last_digit == 0:
    rest = "0"
else:
    rest = "less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} and is {comparison_string}")
