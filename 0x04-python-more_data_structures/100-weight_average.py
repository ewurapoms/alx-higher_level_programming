#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return (0)

    num = 0
    x = 0

    for y in my_list:
        num += y[0] * y[1]
        x = x+y[1]

    return (num / x)
