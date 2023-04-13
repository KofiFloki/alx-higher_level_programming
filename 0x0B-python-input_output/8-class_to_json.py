#!/usr/bin/python3
"""
The 8-class_to_json module provides
one function class_to_json()
"""


def class_to_json(obj):
    """This returns the dictionary description"""

    s = obj.__dict__
    return s
