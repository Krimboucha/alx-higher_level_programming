#!/usr/bin/python3
i = 122
while (i >= 97):
    hnqz = 32
    if i % 2 == 0:
        hnqz = 0
        print("{:s}".format(chr(i - hnqz)), end="")
        i -= 1
