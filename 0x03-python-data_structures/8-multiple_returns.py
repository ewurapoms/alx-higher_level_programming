#!/usr/bin/python3

def multiple_returns(sentence):
    str_len = len(sentence)

    if (str_len == 0):
        tup = (str_len, None)
    else:
        tup = (str_len, sentence[0])

    return (tup)
