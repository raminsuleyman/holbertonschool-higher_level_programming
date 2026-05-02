#!/usr/bin/python3
"""abstract shape kalsi"""
from abc import ABC, abstractmethod
import math as m


class Square(ABC):
    """fiqurlarin abstract kalsi"""

    @abstractmethod
    def area(self):
        """saheni qaytarir"""
        pass

    @abstractmethod
    def perimeter(self):
        """perimetri qayatrir"""
        pass

class Circle(Square):
    """fiqur klassindan miras alan cevre subklasi"""
    def __init__(self, radius):
        """radiusu tapir"""
        self.radius = abs(radius)

    def area(self):
        """saheni qayatrir"""
        return m.pi * (self.radius ** 2)

    def perimeter(self):
        """perimetri qayatrir"""
        return 2 * m.pi * self.radius

class Rectangle(Square):
    """fiqur klssindan miras alan duzbucaqli subklasi"""

    def __init__(self, width, height):
        """duzbucaqlinin yaradilmasi"""
        self.width = width
        self.height = height

    def area(self):
        """sahenin qaytarilmasi"""
        return self.width * self.height

    def perimeter(self):
        """perimetrin qaytarilmasi"""
        return 2* (self.width + self.height)

def shape_info(shape):
    """print area and perimeter"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
