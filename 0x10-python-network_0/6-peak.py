#!/usr/bin/python3
""" Defines a function find_peak """


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers
    Args:
        list_of_integers(list): list of integers
    """
    if list_of_integers:
        n = len(list_of_integers)
        peak = list_of_integers[0]
        for i in range(int(n / 2) - 1, -1, -1):
            left = i * 2 + 1
            right = i * 2 + 2
            if left < n and list_of_integers[left] > peak:
                peak = list_of_integers[left]
            if right < n and list_of_integers[right] > peak:
                peak = list_of_integers[right]
            if list_of_integers[i] > peak:
                peak = list_of_integers[i]
        return peak
