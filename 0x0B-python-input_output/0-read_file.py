#!/usr/bin/python3
""" read_file function
"""


def read_file(filename=""):
    """ reads a file and print its content to stdout
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(f"{file.read()}", end="")
