#!/usr/bin/python3
"""base-geometry-den miras alan rectangle kalsi"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry istifade ederek duzbucaqli"""

    def __init__(self, width, height):
        """Yeni rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
