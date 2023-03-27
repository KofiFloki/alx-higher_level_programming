#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    b = 0
    try:
        for c in range(x):
            print(my_list[c], end=' ')
            b += 1
    except IndexError:
        pass
    finally:
        print(('\n'), end=' ')
        return b
