#!/usr/bin/python3
"""
Bu modul 'say_my_name' funksiyasını təqdim edir.
"""


def say_my_name(first_name, last_name=""):
    """
    İstifadəçinin ad və soyadını ekrana çap edir.

    Arqumentlər:
        first_name (str): İlk ad.
        last_name (str, optional): Soyad. Default olaraq "".

    Xətalar:
        TypeError: first_name və ya last_name string deyilsə.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
