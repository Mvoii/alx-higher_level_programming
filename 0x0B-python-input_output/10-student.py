#!/usr/bin/env python3

"""Write a class reps student"""

class Student:
    """defines a student class"""
    def __init__(self, first_name, last_name, age):
        """init student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dict rep of student"""
        if attrs is None:
            return self.__dict__
        
        else:
            dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    dict[attr] = getattr(self, attr)
            return dict