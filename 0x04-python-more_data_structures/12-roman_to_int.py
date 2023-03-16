#!/usr/bin/python3
def roman_to_int(roman_string):
    dictionary = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    rom_num = 0
    a = 0
    while a < len(roman_string):
        if a + 1 < len(roman_string) and roman_string[a:a+3] in dictionary:
            rom_num = rom_num + dictionary[roman_string[a:a-1]]
        else:
            rom_num = rom_num + dictionary[roman_string[a]]
            a = a + 1
    return (rom_num)
