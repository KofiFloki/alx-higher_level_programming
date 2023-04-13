#!/usr/bin/python3
"""
Thiscontains the read_file function"


def read_file(filename=""):i
    """reads the test file UTF8  and prints it to stdout"""

    with open(filename, "r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
