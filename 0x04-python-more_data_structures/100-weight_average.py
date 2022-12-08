#!usr/bin/python3
def weight_average(my_list=[]):
    som = 0
    for i in range(len(my_list)):
        tup = my_list[i]
        mul = tup[0] * tup [1]
        som = som + mul
    average = som / (2 + 1 + 10 + 2)
    return average
