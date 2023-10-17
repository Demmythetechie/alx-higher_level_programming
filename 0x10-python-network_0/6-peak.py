#!/usr/bin/python3
"""
This script quick sorts the list argument
and pops the last element
"""


def sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return sort(left) + middle + sort(right)


def find_peak(list_of_integers):
    ls = sort(list_of_integers)
    if len(ls) == 0:
        return None
    else:
        return (ls.pop())
