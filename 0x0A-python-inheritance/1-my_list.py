#!/usr/bin/env python3

"""the module is 1-my_list"""

class Mylist(list):
    """class Mylist"""
    def __init__(self):
        """init"""
        super().__init__()

    def print_sorted(self):
        """print_sorted"""
        print(sorted(self))