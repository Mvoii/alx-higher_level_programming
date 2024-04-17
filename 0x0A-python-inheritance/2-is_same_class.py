#!/usr/bin/python3

"""The module is 2-is_same_class"""


def is_same_class(obj, a_class):
    """
    Function Doc

    Args:
        obj (obj): object 1
        a_class (obj): object 2

    Returns:
        bool: if same True else False
    """
    return type(obj) is a_class