#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is not None and tuple_b is not None:
        if len(tuple_a) != 0 or len(tuple_b) != 0:
            if len(tuple_a) < 2 and len(tuple_b) == 0:
                return ((tuple_a[0], 0))
            elif len(tuple_a) == 0 and len(tuple_b) < 2:
                return ((tuple_b[0], 0))
            elif len(tuple_a) == 0:
                return ((tuple_b[0], tuple_b[1]))
            elif len(tuple_b) == 0:
                return ((tuple_a[0], tuple_a[1]))
            elif len(tuple_a) < 2 and len(tuple_b) < 2:
                return ((tuple_a[0] + tuple_b[0], 0))
            elif len(tuple_a) < 2:
                return ((tuple_a[0] + tuple_b[0], tuple_b[1]))
            elif len(tuple_b) < 2:
                return ((tuple_a[0] + tuple_b[0], tuple_a[1]))
            else:
                return ((tuple_a[0] + tuple_b[0], tuple_b[1] + tuple_a[1]))
        else:
            return ((0, 0))
