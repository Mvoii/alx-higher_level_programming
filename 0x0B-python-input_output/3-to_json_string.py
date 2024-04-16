#!/usr/bin/env python3

"""To JSON String"""
import json
"""JSON module"""

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)