#!/usr/bin/python3
"""
This is the module "4-print_square"
This module take in one function, print_square()
This function takes one parameter used as the size of a square to print using #
"""


def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    x = 0
    y = 0
    while x < size:
        while y < size:
            print("#", end="")
            y += 1
        y = 0
        x += 1
        print()
