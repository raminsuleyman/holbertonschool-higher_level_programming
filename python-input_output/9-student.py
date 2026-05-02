#!/usr/bin/python3
"""student to json"""


class Student:
    """Tələbə məlumatlarını saxlayan və JSON formatına hazırlayan klas"""

    def __init__(self, first_name, last_name, age):
        """İnisiatizasiya metodu (obyekt yaradılarkən işləyir)"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Student instansiyasının lüğət təsvirini qaytarır"""
        return self.__dict__
