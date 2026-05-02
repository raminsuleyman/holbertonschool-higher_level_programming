#!/usr/bin/python3
"""sahenin hesablanmasi"""


class BaseGeometry:
    """hendesi fiqurlarin sehesi"""

    def area(self):
        """saheni hesablayan metod"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """deyerin tam qiymet oldugunu yoxlayir"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
