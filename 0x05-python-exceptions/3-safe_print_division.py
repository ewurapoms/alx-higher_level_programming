#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        div = None
    finally:
        try:
            print("Inside result: {}".format(result))
        except (NameError):
            pass
    return (div)
