#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    num = len(argv) - 1

    if num == 0:
        print("0 arguments.")
    elif num == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num))

    for x, y in enumerate(argv[1:]):
        print("{}: {}".format(x + 1, y))
