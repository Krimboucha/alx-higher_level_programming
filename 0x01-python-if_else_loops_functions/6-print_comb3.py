#!/usr/bin/python3
sep = ", "
for i in range(10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            sep = "\n"
            print("{}".format(sep))
        print("{}{}".format(i,j), end=sep)
#        else:
#        print(", ", end="")
