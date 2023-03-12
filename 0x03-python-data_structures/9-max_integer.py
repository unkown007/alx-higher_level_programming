#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None:
        size = len(my_list)
        if size != 0:
            m = my_list[0]
            for i in range(1, size):
                if my_list[i] > m:
                    m = my_list[i]
            return (m)
