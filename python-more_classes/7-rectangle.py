#!/usr/bin/python3
"""Düzbucaqlı modulu."""


class Rectangle:
    """Düzbucaqlı klası.

    Attributes:
        number_of_instances (int): Yaradılmış obyektlərin sayı.
        print_symbol (any): Düzbucaqlını çəkmək üçün istifadə olunan simvol.
    """

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
        """print_symbol ilə düzbucaqlını vizual təmsil edir."""
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)
        rect_lines = []
        for i in range(self.__height):
            rect_lines.append(symbol * self.__width)
        return "\n".join(rect_lines)

    def __repr__(self):
        """Obyektin kod təmsili."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Obyekt silinəndə mesaj verir."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
