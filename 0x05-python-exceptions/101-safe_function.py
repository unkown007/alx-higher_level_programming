#!/usr/bin/python3
def safe_function(fct, *args):
    res = None
    try:
        res = fct(*args)
    except (TypeError, ValueError, IndexError, ZeroDivisionError) as te:
        import sys
        print("Exception: {}".format(te))
        return (None)
    else:
        return (res)
