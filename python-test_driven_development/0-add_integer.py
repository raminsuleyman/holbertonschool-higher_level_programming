#!/usr/bin/python3
"""
This module provides the 'add_integer' function.
"""


def add_integer(a, b=98):
    """
    Adds two numbers. Raises TypeError for NaN or Infinity.
    """

    # 1. Type checking (for list, string, etc.)
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # 2. Value checking (NaN and Infinity)
    # NaN is not equal to itself (a != a).
    # Infinity is detected using float('inf').
    if a != a or abs(a) == float('inf'):
        raise TypeError("a must be an integer")
    if b != b or abs(b) == float('inf'):
        raise TypeError("b must be an integer")

    # 3. Safe conversion and addition
    return int(a) + int(b)
