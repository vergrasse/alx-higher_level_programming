#!/usr/bin/python3
"""load_from_json_file module.

Contains a function that creates an object from a "JSON file".
"""
import json


def load_from_json_file(filename):
    """Creates an object from a "JSON file"."""
    with open(filename, 'r') as f:
        return json.load(f)
