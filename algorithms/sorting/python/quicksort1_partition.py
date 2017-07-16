#!/bin/python3
import sys

#def partition(a, p, r):    
#    """
#    This solution should work as well. 
#    in-place    
#    """
#    x = a[p]
#    i = p - 1
#    for j in range(p + 1, r):
#        if a[j] <= x:
#            i = i + 1
#            a[i], a[j] = a[j], a[i]    
#    print(*a, sep=' ')
        
def partition(a, p, r):    
    pivot = a[p]
    right = []
    left = []
    for j in range(p + 1, r):
        if a[j] <= pivot:
            right.append(a[j])
        else:
            left.append(a[j])
    print(*right, pivot, *left, sep=' ')

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
p = 0
r = len(arr)

partition(arr, p, r)

