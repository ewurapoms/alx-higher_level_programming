#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    if a_dictionary:
        for m, n in list(a_dictionary.items()):
            if n == value:
                del a_dictionary[m]
    return (a_dictionary)
