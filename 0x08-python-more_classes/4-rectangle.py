#!/usr/bin/python3
"""
this is the 4-rectangle Module
which provides the class Rectangle
the rectangle has two attributes width and height
"""


class Rectangle:
    """defines the class"""

    def __init__(self, width=0, height=0):
        """
        this defines the attribute of width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieves the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        retrieves the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        x = 0
        y = 0
        z = ""
        if self.__width == 0 or self.__height == 0:
            return z
        while y < self.__height:
            while x < self.width:
                z += "#"
                x += 1
            y += 1
            x = 0
            if y < self.__height:
                z += "\n"
        return z

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
