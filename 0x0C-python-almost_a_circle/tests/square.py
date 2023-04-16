#!/usr/bin/python3
"""
This is a Square which inherits from Rectangle
"""


from models.rectangle import Rectangle
"""this imports the rectangle module"""


class Square(Rectangle):
    """defines the class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a string representation in a format"""
        s = "[Square] ({:d}) {:d}/{:d} - {:d}"
        r = s.format(self.id, self.x, self.y, self.width)
        return r

    @property
    def size(self):
        """retrieves the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary representation"""
        s = {}
        s['id'] = self.id
        s['size'] = self.width
        s['x'] = self.x
        s['y'] = self.y
        return s
