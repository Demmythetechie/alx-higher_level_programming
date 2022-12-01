#!/usr/bin/python3
def uppercase(str):
    for ind in range(len(str) + 1):
        value = ord(str[ind])

        if ind != len(str) - 1:

            if value != value - 32 and (value < 123 and value > 97):
                value = value - 32
            else:
                value = ord(str[ind])

            print("{}".format(chr(value)), end='')

        elif ind == len(str) + 1:

            print("")
