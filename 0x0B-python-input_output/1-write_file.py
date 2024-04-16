#!/usr/bin/env python3

"""Write a string from a text file"""

def write_file(filename="", text=""):
    """
    a function that writes a string to a textfile (UTF8) and returns the number of characters written

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """
    
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)