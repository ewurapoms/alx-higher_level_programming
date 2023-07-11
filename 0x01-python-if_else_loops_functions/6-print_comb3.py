#!/usr/bin/python3
for pos_c in range(0, 9):
    for pos_d in range(pos_c + 1, 10):
        if pos_c == 8:
            print("{:d}{:d}".format(pos_c, pos_d))
            break
        print("{:d}{:d}".format(pos_c, pos_d), end=", ")
