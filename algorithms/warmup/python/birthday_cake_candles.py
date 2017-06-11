#!/bin/python3

import sys

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = ar.count(max(ar))
print(result)