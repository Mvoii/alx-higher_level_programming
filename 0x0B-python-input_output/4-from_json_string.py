#!/usr/bin/env python3

"""converting from JSON string to py data structure"""

import json
"""
provides the function json.loads() to convert 
a JSON string to a Python data structure
"""

def from_json_string(my_str):
    """
    returns an object (Python data structure) 
    represented by a JSON string
    """
    return json.loads(my_str)