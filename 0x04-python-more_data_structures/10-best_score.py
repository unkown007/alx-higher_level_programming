#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        items = list(a_dictionary.items())
        size = len(items)
        if size > 0:
            max_item = items[0][1]
            idx = 0
            for i in range(1, size):
                if max_item < items[i][1]:
                    max_item = items[i][1]
                    idx = i
            return items[idx][0]
