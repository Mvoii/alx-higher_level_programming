#!/usr/bin/env python3

"""write a class"""

class Student:
    """Defines a class Student"""
    def __init__(self, first_name, last_name, age):
        """initializes the attributes of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dict rep of student"""
        return self.__dict__