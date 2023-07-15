#!/usr/bin/python3

def no_c(my_string):
    size = len(my_string)

    m = 0

    new = my_string[:]

    for i in range(size):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            new = new[:(i - m)] + my_string[(i + 1):]
            m = m + 1

    return (new)
