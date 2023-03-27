#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError as ve:
        print("{}".format(ve), file=sys.stderr)
        return (False)
    except TypeError as te:
        print("{}".format(te), file=sys.stderr)
        return (False)
