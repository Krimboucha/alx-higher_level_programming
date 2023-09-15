#!/usr/bin/python3
"""Defines a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle
            x (int): x coordinate of the Rectangle
            y (int): y coordinate of the Rectangle
            id (int): id of the Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
	"""sets the width of the rectangle"""
        self.__width = value

    @property
    def height(self):
        """gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
	"""sets the height of the rectangle"""
        self.__height = value

    @property
    def x(self):
        """gets the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
	"""sets the x coordinate of the rectangle"""
        self.__x = value

    @property
    def y(self):
        """gets the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
	"""sets the y coordinate of th rectangle"""
        self.__y = value
