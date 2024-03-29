#!/usr/bin/python3
"""to_json_string module.

Contains a function that returns the JSON representation of an object (string).
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    """
    import json

    return json.dumps(my_obj)
