#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        new_string = ""
        for x in my_string:
            if x != 'c' and x != 'C':
                new_string += x
        return (new_string)
    return (None)
