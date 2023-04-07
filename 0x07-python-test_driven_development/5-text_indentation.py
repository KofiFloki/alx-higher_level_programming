#!/usr/bin/python3
"""
This 5-text indentation module defines one function, text_indentation().
The function takes one parameter as a string of text and
prints the text with 2 lines after each "." or "?"
"""



def print_square(size):
    """prints a square using the character '#'"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    a = 0
    b = 0
    while a < size:
        while b < size:
            print("#", end="")
            b += 1
        b = 0
        a += 1
        print()
