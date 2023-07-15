#!/usr/bin/python3

def max_integer(my_list=[]):
    size = len(my_list)

    if size == 0:
        return (None)

    biggest = my_list[0]

    for m in range(1, size):
        if my_list[m] > biggest:
            biggest = my_list[i]

    return (biggest)
