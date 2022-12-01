#!/usr/bin/python3
def fizzbuzz():
    for mul in range(1, 101):
        if mul % 3 == 0:
            print("Fizz", end='')
        if mul % 5 == 0:
            print("Buzz", end='')
        if mul % 3 != 0 and mul % 5 != 0:
            print(mul, end='')
        print(" ", end='')
