#!/usr/bin/python3
def print_list_integer(mylist=[]):
    ls = [int(mylist[i]) for i in range(len(mylist))]
    for n in range(len(ls)):
        print("{}".format(ls[n]))
