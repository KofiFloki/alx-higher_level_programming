#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)

    if num_args == 0:
        print("Number of arguments: 0.")
        print(".")
    elif num_args == 1:
        print("Number of argument: 1.")
        print("1: " + args[0])
    else:
        print("Number of arguments: " + str(num_args) + ".")
        for i, arg in enumerate(args):
            print(str(i+1) + ": " + arg)
