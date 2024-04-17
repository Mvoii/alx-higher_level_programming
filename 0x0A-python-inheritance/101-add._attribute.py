#!/usr/bin/env python3

"""function that adds a new attr to an obj if its possible"""

def add_attribute(obj, name, value):
    """adds new attr to an obj"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("Can't add new attribute")
    setattr(obj, name, value)