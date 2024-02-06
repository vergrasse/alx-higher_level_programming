#!/usr/bin/python3
"""write_file module.

Contains a function that writes a string to a text file.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written."""
    # Open the file in write mode (overwriting existing content) or create it if it doesn't exist
    with open(filename, mode='w', encoding='utf-8') as file:
        # Write the text to the file
        file.write(text)
        # Return the number of characters written
        return len(text)
