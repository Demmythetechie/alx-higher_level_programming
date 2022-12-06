#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for n in range(len(matrix[i])):
            if n != 0 and n != len(matrix[i]):
                print("{}".format(' '), end='')
            print("{:d}".format(matrix[i][n]), end='')
        print("{}".format('\n'), end='')
