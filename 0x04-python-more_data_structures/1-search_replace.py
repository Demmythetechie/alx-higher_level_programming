#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ls = [my_list[x] for x in range(len(my_list))]
    for i in range(len(ls)):
        if ls[i] == search:
            ls[i] = 89
        else:
            pass
    return ls
