#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

s =  [1 if a > 0 else -1 if a < 0 else 0 for a in arr]
print(s.count(1)/n, s.count(-1)/n, s.count(0)/n, sep='\n')