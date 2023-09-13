#!/usr/bin/python3
"""defines a json str function"""
import json


def from_json_string(my_str):
    """returns the object represented by a JSON string"""
    return json.loads(my_str)
