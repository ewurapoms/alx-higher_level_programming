#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as exc:
        print('Exception:', exc, file=__import__('sys').stderr)
        return (False)
