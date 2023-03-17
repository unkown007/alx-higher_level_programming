#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }
    check_count = ['V', 'L', 'D']
    if roman_string is None or type(roman_string) != str:
        return (0)
    for x in roman_string:
        if x not in roman:
            return (0)
    for c in check_count:
        if roman_string.count(c) > 1:
            return (0)
    size = len(roman_string)
    count = 1
    letter = roman_string[0]
    for i in range(1, size):
        if roman_string[i] != letter:
            count = 0
            letter = roman_string[i]
        else:
            count = count + 1
            if count > 3:
                return (0)
    i = 0
    number = 0
    a, b = 0, 0
    while i < size:
        a = roman[roman_string[i]]
        if (i + 1) < size:
            i = i + 1
            b = roman[roman_string[i]]
            if b > a:
                number = number + (b - a)
            else:
                number = number + (b + a)
        else:
            number = number + a
        i = i + 1
    return (number)
