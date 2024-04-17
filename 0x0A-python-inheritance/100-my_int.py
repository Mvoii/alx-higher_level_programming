#!/usr/bin/env python3

"""Write a class MyInt that inherits from int"""

class MyInt(int):
    """A suclass of the class int"""
    def __eq__(self, other):
        """sets the behavious of the == operator"""
        return int(self) != other

    def __ne__(self, other):
        """sets the != behaviour"""
        return int(self) == other