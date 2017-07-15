#!/bin/python3
import sys

def insertion_sort(a):
    c = 0
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
            c = c + 1
        a[i + 1] = key
    print(c)    

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

insertion_sort(arr)