#!/usr/bin/python3
"""
This is the `7-base_geometry' module
with just one class BaseGeometry()
"""


class BaseGeometry:
    """defines a class called BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
