#!/usr/bin/python3
"""senedlesme"""


class Rectangle:
    """duzbucaqlinit yaradiriq"""
    def __init__(self, width=0,  height=0):
        """en ve hundurluk"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """eni geyi qaytarirriq"""
        return self.__width

    @width.setter
    def width(self, value):
        """deyeri yoxluyuruq"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """eni geyi qaytarirriq"""
        return self.__height

    @height.setter
    def height(self, value):
        """deyeri yoxluyuruq"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """saheni qaytaririq"""
        return self.__width * self.__height

    def perimeter(self):
        """perimetr qaytaririq"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
