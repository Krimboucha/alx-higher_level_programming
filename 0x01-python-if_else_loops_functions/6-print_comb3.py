#!/usr/bin/python3
sep = ", "
for i in range(10):
    for j in range(i + 1, 10):
        print(f"{i}{j}", end=sep)
        if i == 8 and j == 9:
            sep = "\n"
            print(f"{sep}")
#        else:
#        print(", ", end="")
