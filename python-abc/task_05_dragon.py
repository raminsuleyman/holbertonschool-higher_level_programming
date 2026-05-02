#!/usr/bin/python3
"""This module contains a class Dragon."""
from abc import ABC, abstractmethod


class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin():
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
