#!/usr/bin/python3
def _reduce(fn, seq, init=0):

    try:
        return _reduce(fn, seq[1:], fn(init, seq[0]))
    except IndexError:
        return (init)


def roman_to_int(roman_string):

    temp = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
    }
    try:
        num = list(map(temp.get, roman_string[::-1]))
        i = num[0]
    except (IndexError, KeyError, TypeError):
        return (0)

    for x in range(len(num[1:])):
        if num[x + 1] >= num[x]:
            i += num[x + 1]
        else:
            i -= num[x + 1]

    return (i)
