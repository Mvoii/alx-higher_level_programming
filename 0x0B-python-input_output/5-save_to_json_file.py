#!/usr/bin/env python3

"""Write and convert to a json string"""

import json
"""provides functions for reading and writing JSON data"""

def save_to_json_file(my_obj, filename):
    """
    a function to write an object to a text file,
    using JSON representation
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)