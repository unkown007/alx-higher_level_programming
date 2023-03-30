#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    printed = 0
    if my_list is not None:
        for i in range(0, x):
            try:
                print("{:d}".format(my_list[i]), end="")
                printed += 1
            except IndexError:
                continue
    print()
    return (printed)
