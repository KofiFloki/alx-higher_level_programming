#!/usr/bin/python3
"""
The `8-rectangle' module has just two classes,
BaseGeometry() and Rectangle which is a sub
class of BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
imports the super class
"""


class Rectangle(BaseGeometry):
    """defines a class Rectangle which is a subclass of BaseGeometry"""
    def __init__(self, width, height):
        """validates and initializes width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area"""
        return self.__width * self.__height

    def __str__(self):
        s = ""
        s += "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
        return s
