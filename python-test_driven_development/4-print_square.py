#!/usr/bin/python3
"""
Bu modul 'print_square' funksiyasını təqdim edir.
"""


def print_square(size):
    """
    Ekrana '#' işarələri ilə kvadrat çəkir.

    Arqumentlər:
        size (int): Kvadratın tərəfinin uzunluğu.

    Xətalar:
        TypeError: size tam ədəd (int) deyilsə.
        ValueError: size 0-dan kiçikdirsə.
    """
    # 1. Tip yoxlanışı (float da daxil olmaqla hər şeyi kəsir)
    if type(size) is not int:
        raise TypeError("size must be an integer")
    # 2. Dəyər yoxlanışı (mənfi rəqəmlər)
    if size < 0:
        raise ValueError("size must be >= 0")

    # 3. Kvadratın çəkilməsi
    # Əgər size 0-dırsa, range(0)
    for i in range(size):
        print("#" * size)
