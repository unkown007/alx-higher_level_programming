#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new_dictionary = {}
        for key in a_dictionary:
            new_dictionary[key] = a_dictionary[key] * 2
        return (new_dictionary)
