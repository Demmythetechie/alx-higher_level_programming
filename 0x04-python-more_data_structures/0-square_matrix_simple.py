#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    for i in range(len(matrix)):
        n_matrix.append([])
        for x in range(len(matrix[i])):
            n_matrix[i].append(matrix[i][x] ** 2)
    return n_matrix
