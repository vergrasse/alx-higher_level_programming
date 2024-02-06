#!/usr/bin/python3
"""write_file module.

Contains a function that writes a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.
    If the file doesn’t exist, it should be created.
    The function should overwrite the content of the file if it already exists.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
