#!/usr/bin/python3
"""Define a rectangle class"""


class Rectangle:
    """A class representing a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with a given width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Calculate the area of the rectangle"""
        return self._width * self._height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        if self._width == 0 and self._height == 0:
            return 0
        return 2 * (self._width + self._height)
