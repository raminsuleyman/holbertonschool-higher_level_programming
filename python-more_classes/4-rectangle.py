#!/usr/bin/python3
"""Düzbucaqlı modulu."""


class Rectangle:
    """Düzbucaqlı klası."""

    def __init__(self, width=0, height=0):
        """İnit metodu."""
        self.width = width
        self.height = height

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
        """Vizual olaraq # simvolları ilə qaytarır."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            rect.append("#" * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        """Obyektin yenidən yaradıla bilən sətir formasını qaytarır."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
