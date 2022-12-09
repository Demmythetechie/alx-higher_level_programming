#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ls = [i for i in a_dictionary if value == a_dictionary[i]]
    if len(ls) == 0:
        pass
    else:
        for n in range(len(ls)):
            del a_dictionary[ls[n]]
    return a_dictionary
