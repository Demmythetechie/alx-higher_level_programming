#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    import hidden_4
    ls = dir(hidden_4)
    ls.sort()
    for i in range(len(ls)):
        if ls[i][i] == '_':
            pass
        else:
            print("{}".format(ls[i]))
