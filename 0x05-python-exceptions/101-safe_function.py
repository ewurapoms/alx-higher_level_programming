#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        output = fct(*args)
    except Exception as m:
        sys.stderr.write("Exception: {}\n".format(m))
        output = None

    return (output)
