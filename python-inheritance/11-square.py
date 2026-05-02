#!/usr/bin/python3
"""Rectangleden miras alan square klassi"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """"rectangleden square yaradilmasi"""

    def __init__(self, size):
        """kvadratin yaradilmasi"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """kvadratin sahesini qayatrir"""
        return self.__size ** 2

    def __str__(self):
        """string kimi qaytarilmasi"""
        return "[Square] {}/{}".format(self.__size, self.__size)
