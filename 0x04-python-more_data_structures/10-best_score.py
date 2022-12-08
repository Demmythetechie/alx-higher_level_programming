#!/usr/bin/python3
def best_score(a_dictionary):
    ls = []
    x = 0
    w = 1
    for
    i in a_dictionary:
        ls[x] = i
        x = x + 1

    for n in a_dictionary:
        if a_dictionary[n] > a_dictionary[ls[w]]:
            return n
        else:
            pass
        w = w + 1

