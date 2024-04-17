#!/usr/bin/env python3

"""the module is 2-is_same_class"""

def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class"""
    return type(obj) is a_class