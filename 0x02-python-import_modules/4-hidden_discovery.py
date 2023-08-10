#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    listOfNames = dir(hidden_4)
    for name in listOfNames:
        if name[0] != "_":
        print("{:s}".format(name))
