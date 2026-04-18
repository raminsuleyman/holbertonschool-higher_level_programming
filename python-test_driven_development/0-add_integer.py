#!/usr/bin/python3
"""
Bu modul 'add_integer' funksiyasını təqdim edir.
"""


def add_integer(a, b=98):
    """
    İki rəqəmi toplayır. NaN və ya Infinity üçün TypeError qaytarır.
    """
    # 1. Tip yoxlanışı (Siyahı, string və s. üçün)
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # 2. Dəyər yoxlanışı (NaN və Infinity üçün)
    # NaN özünə bərabər deyil (a != a).
    # Infinity isə mütləq dəyərinə görə sonsuzdur.
    if a != a or abs(a) == float('inf'):
        raise TypeError("a must be an integer")
    if b != b or abs(b) == float('inf'):
        raise TypeError("b must be an integer")

    # 3. İndi təhlükəsiz şəkildə çevirib toplaya bilərik
    return int(a) + int(b)
