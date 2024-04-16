#!usr/bin/env python3

"""search and update"""

def append_after(filename="", search_string="", new_string=""):
    """
    functions tha tinserts a line os text to a file
    after each line conating a specific string
    Args:
        - filename: the file to search
        - search_string: the string to search
        - new_string: the string to add
    """
    with open(filename, 'r') as foo:
        text = foo.readlines()

    with open(filename, 'w') as bar:
        string = ""
        for line in text:
            if search_string in line:
                string += new_string
        bar.write(string)