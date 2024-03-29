#!/usr/bin/python3
""" Rectangle module
"""
from base import Base


class Rectangle(Base):
    """ Defines a Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes a Rectangle instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width's getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """ width's setter
        """
        if not isinstance(width, int):
            raise TypeError("Width must be an integer")
        if width <= 0:
            raise ValueError("Width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ height's getter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """ height's setter
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ x's getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """ x's setter
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ y's getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """ y's setter
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of a rectangle
        """
        return self.__width * self.__height

    def display(self):
        """ displays a rectangle with '#'
        """
        for i in range(heigth):
            for j in range(width):
                print("#", end="")
            print("")
