#!/usr/bin/python3
"""Student to disk and reload"""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary """
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            res = {}
            for k in attrs:
                if hasattr(self, k):
                    res[k] = getattr(self, k)
            return res
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes"""
        for key, value in json.items():
            setattr(self, key, value)
