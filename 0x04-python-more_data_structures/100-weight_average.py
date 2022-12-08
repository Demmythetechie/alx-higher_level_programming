#!/usr/bin/python3
def weight_average(my_list=[]):
    som = 0
    num = 0
    for i in range(len(my_list)):
        tup = my_list[i]
        num = num + tup[1]
        mul = tup[0] * tup [1]
        som = som + mul
    average = som / num
    return average
