#!/usr/bin/python3
def no_c(my_string):
    ln = len(my_string)
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            pass
        else:
            my_string = my_string + my_string[i]

    my_str = my_string[ln:]
    return my_str
