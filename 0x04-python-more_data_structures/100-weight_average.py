#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        size = len(my_list)
        if size > 0:
            list_prod = [x * y for x, y in my_list]
            list_div = [y for x, y in my_list]
            if sum(list_div) != 0:
                return (sum(list_prod) / sum(list_div))
        else:
            return (0)
