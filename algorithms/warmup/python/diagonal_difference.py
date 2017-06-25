#!/bin/python3

import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

n = len(a)
d1 = sum(a[i][i] for i in range(n))
d2 = sum(a[i][n-i-1] for i in range(n))
print(abs(d1-d2))
