#!/usr/bin/python3
def best_score(a_dictionary):
    if bool(a_dictionary):
        w = 1
        ls = list(a_dictionary)
        st = ls[0]
        for i in range(len(ls) - 1):
            if a_dictionary[st] > a_dictionary[ls[w]]:
                pass
            else:
                st = ls[w]
            w = w + 1
        return st
    else:
        return None
