#!/usr/bin/python3
"""
This module contains a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Adds 2 integers.

    Args:
    a (int): The first integer.
    b (int): The second integer. Defaults to 98 if not provided.

    Returns:
    int: The addition of a and b.

    Raises:
    TypeError: If a or b is not an integer or float.

    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
