#!/usr/bin/env python3

"""Read from file"""

def read_file(filename=""):
    """Reads text from the file adn prints to stdout"""
    with open(filename) as file:
        content = file.read()
    print(content, end="")