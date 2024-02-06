#!/usr/bin/python3
""" write_file module
"""


def write_file(filename="", text=""):
    """ writes a text to file
    """
    with open(filename, "w", encoding="utf-8") as file:
        num_chars = file.write(text)
        return num_chars
