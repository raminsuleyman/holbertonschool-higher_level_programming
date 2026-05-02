#!/usr/bin/python3
"""ABC class ANimal"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstarct animal kalssi"""

    @abstractmethod
    def sound(self):
        """Heyvanin cixardigi ses"""
        pass

class Dog(Animal):
    """dig klassi animaldan miras alir"""
    def sound(self):
        """itin sesini qaytarir"""
        return "Bark"

class Cat(Animal):
    """cat klasi animaldan miras alir"""
    def sound(self):
        """pisik sesi qayatrir"""
        return "Meow"
