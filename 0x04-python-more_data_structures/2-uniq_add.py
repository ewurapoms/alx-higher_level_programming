#!/usr/bin/python3

def uniq_add(my_list=[]):

    temp = set(my_list)
    n = 0

    for x in temp:
        n = n+x

    return (n)
