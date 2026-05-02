#!/usr/bin/python3
"""
Çoxlu mirasalmanı nümayiş etdirən Fish, Bird və FlyingFish klasları.
"""


class Fish:
    """Balıq klası."""
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Quş klası."""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Həm Fish, həm də Bird-dən miras alan Uçan Balıq klası."""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
