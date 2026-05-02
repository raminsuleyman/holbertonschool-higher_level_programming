#!/usr/bin/python3
"""fayla metn yazmaq"""


def write_file(filename="", text=""):
    """utf8 formati"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
