#!/usr/bin/python3
"""obyektin mirsa yolu ile gelib-gelmediyini yoxlayir"""


def inherits_from(obj, a_class):
    """obyektin klassdan olub-olmadigini yoxlayir"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
