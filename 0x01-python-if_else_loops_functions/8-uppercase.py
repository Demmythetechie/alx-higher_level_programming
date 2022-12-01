#!/usr/bin/python3
def uppercase(str):
    for ind in range(len(str)):
        value = ord(str[ind])

        if ind != len(str):

            if value != value - 32 and (value < 123 and value > 97):
                value = value - 32
            else:
                value = ord(str[ind])

            print("{}, ".format(chr(value)), end='')

        else:
            print("{}, ".format(chr(value)))
