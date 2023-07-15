#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    n = len(my_list)

    copy = my_list[:]

    if 0 <= idx < n:
        copy[idx] = element

    return (copy)
