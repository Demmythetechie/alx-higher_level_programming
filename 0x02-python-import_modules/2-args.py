#!/usr/bin/python3
if __name__  == '__main__':
    from sys import argv
    print("{} argument".format(0), end='')
    if len(argv) == 1:
        print(".")
    else:
        print(":")

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
