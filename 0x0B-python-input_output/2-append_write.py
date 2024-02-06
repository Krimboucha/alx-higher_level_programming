#!/usr/bin/python3
""" append module
"""


def append_write(filename="", text=""):
    """ appends a text to the end of a file
    """
    with open(filename, "a", encoding="utf-8") as file:
        num_chars = file.write(f"{text}")
        return num_chars
