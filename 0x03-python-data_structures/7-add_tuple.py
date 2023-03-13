#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    A = len(tuple_a)
    B = len(tuple_b)
# check for tuple_a
    if A < 1:
        tuple_a = (0, 0)
    elif A < 2:
        tuple_a = (tuple_a[0], 0)

# check for tuple_b
    if B < 1:
        tuple_b = (0, 0)
    elif B < 2:
        tuple_b = (tuple_b[0], 0)

    tup = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tup
