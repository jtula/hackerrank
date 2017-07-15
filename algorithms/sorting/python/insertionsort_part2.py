#!/bin/python3
import sys

def insertion_sort(a):
    """
    Solution to Insertion Part 2 with loop invariant
    (solution to next exercise - Correctness and the Loop Invariant)
    """
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    print(*a, sep=' ')

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

insertion_sort(arr)