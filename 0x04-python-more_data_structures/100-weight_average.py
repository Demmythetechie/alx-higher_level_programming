#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) != 0:
        som = 0
        num = 0
        for i in range(len(my_list)):
            tup = my_list[i]
            num = num + tup[1]
            mul = tup[0] * tup [1]
            som = som + mul
        average = som / num
    else:
        return 0
    return average
