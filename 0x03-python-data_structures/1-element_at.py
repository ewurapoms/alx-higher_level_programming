#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return (None)

    el_mnt = len(my_list)

    if idx > el_mnt - 1:
        return (None)

    return(my_list[idx])
