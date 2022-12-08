#!/usr/bin/python3
def uniq_add(my_list=[]):
    ls = []
    for i in range(len(my_list)):
        if my_list[i] in ls:
            pass
        else:
            ls.append(my_list[i])
    a = 0
    for x in range(len(ls)):
        a = a + ls[x]
    return a
