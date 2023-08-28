#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
        try:
            return fct(*args)
        except as msg:
            print("Exception: {}".format(msg), file=stderr)
