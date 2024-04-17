#!/usr/bin/env python3

"""the module is 10-square"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

"""Write a class Square that inherits from rectangle"""

class Square(Rectangle):
    """A subclass of rectangle"""
    def __init__(self, size):
        """init private attribute size and validate if int"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def are(self):
        """returns the area of teh square"""
        return self.__size ** 2