#!/usr/bin/python3
"""write-file module

Contains a function that whrite a text file.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns the number of characters added."""
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
