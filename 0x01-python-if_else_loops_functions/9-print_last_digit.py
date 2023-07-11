#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        las = number % 10
    else:
        las = number % -10
        las *= -1

    print("{:d}".format(las), end='')
    return (las)
