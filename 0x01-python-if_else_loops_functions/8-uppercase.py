#!/usr/bin/python3


def uppercase(str):
    print("{}".format(str.translate(
        {(c | 32): c for c in range(ord(65), ord(90) + 1)}
    )))
