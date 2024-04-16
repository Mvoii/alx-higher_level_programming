#!/usr/bin/env python3

"""Class to json"""

def class_to_json(obj):
    """
    a function that returns the dict  description with
    simple data structure
    (list, dictionary, string, integer and boolean)
    from JSON serialization of an object
    Args:
        obj: an instance of a class
        All attributes of teh obj class are serializable
    """
    return obj.__dict__