#!/usr/bin/python3
"""
the '0-lookup' module defines just one function
"""


def lookup(obj):
    """ Defines a function that returns the list of available attributes"""
    return dir(obj)
