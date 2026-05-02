#!/usr/bin/python3
"""Düzbucaqlı modulu."""


class Rectangle:
    """Düzbucaqlılassi"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Yeni düzbucaqlı yaradır."""
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
        """Düzbucaqlını print_symbol ilə vizual təmsil edir."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Obyektin kod təmsili."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Obyekt silinəndə mesaj verir."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """İki düzbucaqlıdan sahəsi böyük olanı qa"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
