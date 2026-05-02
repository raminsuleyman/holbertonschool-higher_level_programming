#!/usr/bin/python3
"""
Rectangle-dan miras alan Square klasını təyin edir.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle-dan istifadə edərək kvadrat təmsil edir."""

    def __init__(self, size):
        """Yeni bir Square yaradır.

        Args:
            size (int): Kvadratın tərəfi.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Kvadratın sahəsini qaytarır."""
        return self.__size ** 2
