#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_delete = []
    for key, val in a_dictionary:
        if val == value:
            keys_to_delete.append(key)
    for key in key_to_delete:
        del a_dictionary[key]
    return a_dictionary