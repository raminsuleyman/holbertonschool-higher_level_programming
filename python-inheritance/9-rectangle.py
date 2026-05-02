#!/usr/bin/python3
"""BaseGeometry miras alan Rectangle kalssi"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """basegeometryden istifade ederek rectangle"""

    def __init__(self, width, height):
        """yeni rectangle klassi"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """duzbucaqlinin sahesini qaytarir"""
        return self.__width * self.__height

    def __str__(self):
        """string teqdimatini qaytarir"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
