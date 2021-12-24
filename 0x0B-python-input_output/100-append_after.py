#!/usr/bin/python3
"""reading from file"""


def append_after(filename="", search_string="", new_string=""):
    """Function inserts a line of text to a file, after each
     line containing a specific string
     Args:
         filename (str): file to be written into
         search_string (str): string to be replaced
         new_string (str): string to be inserted
     Returns: A text file containing the updated texts

     """
    with open(filename) as myfile:
        file = ""
        for line in myfile:
            file += line
            if search_string in line:
                file += new_string
    with open(filename, "w") as myfile:
        myfile.write(file)
