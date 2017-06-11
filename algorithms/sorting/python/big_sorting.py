#!/bin/python3
import sys, math

n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)

unsorted.sort(key=int)

for i in unsorted:
    print(i)