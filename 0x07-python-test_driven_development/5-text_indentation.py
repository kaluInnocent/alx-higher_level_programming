#!/usr/bin/python3
"""Function prints texts"""


def text_indentation(text):
    """
    Function prints a text with 2 lines after each of these characters: '.?:

    Args:
        text (str): Text to be printed

    Returns: Nothing

    """
    if isinstance(text, str):
        text = list(text)
        for i in range(len(text)):
            if text[i] in ".?:" and text[i + 1] == ' ':
                print(text[i], end="")
                text[i + 1] = '\n'
                print(text[i + 1], end="")
            else:
                print(text[i], end="")
    else:
        raise TypeError("text must be a string")
