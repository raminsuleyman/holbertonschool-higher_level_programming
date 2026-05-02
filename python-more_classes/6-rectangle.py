#!/usr/bin/python3
"""Düzbucaqlı modulu."""


class Rectangle:
    """Düzbucaqlılassi"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Yeni düzbucaqlı yaradır və sayı artırır."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Eni qaytarır."""
        return self.__width

    @width.setter
    def width(self, value):
        """Eni təyin edir."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Hündürlüyü qaytarır."""
        return self.__height

    @height.setter
    def height(self, value):
        """Hündürlüyü təyin edir."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Sahəni hesablayır."""
        return self.__width * self.__height

    def perimeter(self):
        """Perimetri hesablayır."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """# ilə vizual təmsil."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            rect.append("#" * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        """Obyektin kod təmsili."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Obyekt silinəndə sayı azaldır və mesaj çap edir."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
