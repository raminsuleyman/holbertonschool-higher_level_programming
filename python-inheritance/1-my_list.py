#!/usr/bin/python3
"""inheritance istifadesi"""


class MyList(list):
    """klass"""

    def print_sorted(self):
        """artan sira ile cap edir"""
        print(sorted(self))
