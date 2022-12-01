#!/usr/bin/python3
def fizzbuzz():
    for mul in range(1, 100):
        if mul % 3 == 0:
            print("Fizz" end='')
        if mul % 5 == 0:
            print("Buzz", end='')
        if mul % 3 != 0 or mul % 5 != 0:
            print(mul)
        if mul % 3 != 0 and mul % 5 != 0:
            print(mul)
        if (mul == 99):
            pass
        else:
            print(" ")
