#!/usr/bin/env python3

"""Write a class rep student"""

class Student:
    """defines student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        
        else:
            dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    dict[attr] = getattr(self, attr)
            return dict
    def reload_from_json(self, json):
        """replaces all attr of student"""
        for keys in json:
            setattr(self, keys, json[keys])