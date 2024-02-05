#!/usr/bin/python3
"""lookup module"""
def lookup(obj):
    """
    Returns a list containing the attributes and methods of the given object.

    Parameters:
    obj (object): The object to inspect.

    Returns:
    list: A list containing the attributes and methods of the object.
    """
    return dir(obj)

