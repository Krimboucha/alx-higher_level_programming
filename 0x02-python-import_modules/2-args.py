#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arg = len(sys.argv) - 1
    arg = " argument"
    if num_arg == 1:
        arg += ":"
        print("{:d}{:s}".format(num_arg, arg))
    elif num_arg == 0:
        arg += "."
        print("{:d}{:s}".format(num_arg, arg))
    else:
        arg += "s:"
        print("{:d}{:s}".format(num_arg, arg))
    i = 1
    while i <= num_arg:
        print("{:d}: {:s}".format(i, sys.argv[i]))
        i += 1
