#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = (number if number > 0 else -number) % 10
lastDigit = lastDigit if number > 0 else -lastDigit
if lastDigit > 5:
    print(f"Last digit of {number} is {lastDigit} and is greater than 5")
elif lastDigit < 6 and lastDigit != 0:
    print(f"Last digit of {number} is {lastDigit} and is less than 6 and not\
 0")
elif lastDigit == 0:
    print(f"Last digit of {number} is {lastDigit} and is 0")
