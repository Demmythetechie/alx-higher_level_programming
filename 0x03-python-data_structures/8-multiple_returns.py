#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) != 0:
        tu = len(sentence), sentence[0]
    else:
        tu = len(sentence), None
    return tu
