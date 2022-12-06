#!/usr/bin/python3
def print_list_integer(mylist=[]):
    ls = [print("{}".format(mylist[i])) for i in range(len(mylist))]
