#!/usr/bin/python3
def multiple_returns(sentence):
    idx = len(sentence)
    if idx == 0:
        return 0, None
    return idx, sentence[0]
