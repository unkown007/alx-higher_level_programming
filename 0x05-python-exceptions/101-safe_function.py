#!/usr/bin/python3
def safe_function(fct, *args):
    res = None
    try:
        res = fct(*args)
    except Exception as ex:
        import sys
        print("Exception: {}".format(ex), file=sys.stderr)
        return (None)
    else:
        return (res)
