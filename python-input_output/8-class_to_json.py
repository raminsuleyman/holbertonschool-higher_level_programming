#!/usr/bin/python3
"""class json"""


def class_to_json(obj):
    """Bir obyektin JSON-a seriyallaşdırıla bilən lüğət təsvirini qaytarır"""
    return obj.__dict__
