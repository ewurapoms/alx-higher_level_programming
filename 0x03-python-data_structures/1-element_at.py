#!/usr/bin/python3

def element_at(my_list, idx):
    if my_list is not None and -1 < idx < len(my_list):
        return my_list[idx]
    return (None)
