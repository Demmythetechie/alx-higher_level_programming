#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        num = my_list[0]
        for i in range(1, len(my_list)):
            if num < my_list[i]:
                num = my_list[i]
            else:
                pass
        return num
