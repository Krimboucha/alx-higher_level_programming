#!/usr/bin/python3
for i in range(100):
    sep = ", "
    if i < 10:
        print("0{:d}".format(i), end=sep)
        continue
    if i == 99:
        sep = "\n"
    print("{:d}".format(i), end=sep)
