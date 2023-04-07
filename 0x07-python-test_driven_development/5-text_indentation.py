#!/usr/bin/python3
"""
This 5-text indentation module defines one function, text_indentation().
The function takes one parameter as a string of text and
prints the text with 2 lines after each "." or "?"
"""


def text_indentation(text):
    """
    Returns the formatted text
    """
    
    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
