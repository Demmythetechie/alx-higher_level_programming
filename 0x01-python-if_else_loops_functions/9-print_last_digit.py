#!/usr/bin/python3
def print_last_digit(number):

    if number < 0:
        last_f = str(number)
        last_s = '-' + last_f[-1]
        last = int(last_s)
        return last
    elif number > 9:
        last = number % 10
        return last
    else:
        return number
