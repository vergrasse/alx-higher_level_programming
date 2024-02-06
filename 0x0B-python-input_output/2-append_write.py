
Below is the implementation of the append_write function according to your requirements:

python
Copy code
#!/usr/bin/python3
"""append_write module.

Contains a function that appends a string to a text file.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns the number of characters added."""
    # Open the file in append mode or create it if it doesn't exist
    with open(filename, mode='a', encoding='utf-8') as file:
        # Write the text to the file
        file.write(text)
        # Return the number of characters added
        return len(text)
