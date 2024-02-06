#!/usr/bin/python3
""" read_file function
"""


def read_file(filename=""):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            read_data = file.read()
            print(read_data)
    except Exception as e:
        print(f"Error reading the file: {e}")
