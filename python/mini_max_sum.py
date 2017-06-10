#!/bin/python3
import sys

arr = list(map(int, input().strip().split(' ')))
s = sum(arr)
print(s - max(arr), s - min(arr))