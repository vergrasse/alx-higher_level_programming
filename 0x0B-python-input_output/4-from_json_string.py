#!/usr/bin/python3
"""from_json_string module.

Contains a function that returns an object (Python data structure) represented by a JSON string.
"""


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.
    """
    import json

    return json.loads(my_str)

