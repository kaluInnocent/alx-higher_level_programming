#!/usr/bin/python3
"""Function prints texts"""


def text_split(text, tags):
    """
    function splits text according to tags
    Args:
        text (str): text to be splitted
        tags (tuple): delimiters
    Returns:
        text4: The text splitted by delimiters
    """
    a, b, c = tags
    line = "\n\n"
    text1 = text.split(a)
    text2 = "{}{}".format(a, line).join(i.lstrip() for i in text1).split(b)
    text3 = "{}{}".format(b, line).join(i.lstrip() for i in text2).split(c)
    text4 = "{}{}".format(c, line).join(i.lstrip() for i in text3)
    return text4


def text_indentation(text):
    """
    Function prints a text with 2 lines after each of these characters: '.?:

    Args:
        text (str): Text to be printed

    Returns: Nothing

    """
    if isinstance(text, str):
        words = text_split(text, ('.', '?', ':'))
        for word in words:
            print(word, end="")
    else:
        raise TypeError("text must be a string")
