#!/usr/bin/env python3

"""Create an object from a json file"""

import json
"""provides functions nessessary"""

def load_from_json_file(filename):
    """a function that creates an object from json"""
    with open(filename, 'r') as file:
        return json.load(file)