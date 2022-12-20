#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        itr = 0
        count = 0
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end='')
            count = count + 1
            itr = itr + 1
        print("")
        return count
    except ValueError:
        itr = itr + 1
        for r in range(itr, x):
            count = count + 1
            print("{:d}".format(my_list[r]), end='')
        print("")
        return count
    except:
        return count
