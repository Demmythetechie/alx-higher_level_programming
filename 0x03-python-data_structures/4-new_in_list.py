#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ls = [my_list[i] for i in range(len(my_list))]
    if idx < 0:
        return ls
    elif idx >= len(ls):
        return ls
    else:
        ls[idx] = element
        return ls
