#!/usr/bin/python3
"""student to json with filter"""


class Student:
    """Filtrləmə qabiliyyəti olan tələbə klası"""

    def __init__(self, first_name, last_name, age):
        """Obyekt yaradılarkən atributları mənimsədir"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Obyektin lüğət təsvirini qaytarır.
        """
        # Bütün atributları lüğət kimi götürürük
        my_dict = self.__dict__

        # Əgər attrs siyahıdırsa və içindəkilər stringdirsə filtr tətbiq edirik
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            # Yalnız attrs siyahısında olan
            filtered_dict = {}
            for key in attrs:
                if key in my_dict:
                    filtered_dict[key] = my_dict[key]
            return filtered_dict

        # Əgər attrs yoxdursa
        return my_dict
