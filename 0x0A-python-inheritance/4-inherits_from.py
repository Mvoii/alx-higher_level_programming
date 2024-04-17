#!/usr/bin/env python3

"""the module is 4-inherits_from"""

def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited from the specified class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class