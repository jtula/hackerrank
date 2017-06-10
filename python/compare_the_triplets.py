#!/bin/python3
import sys

def solve(alice, bob):
   s =  [1 if a > b else -1 if a < b else 0 for a, b in zip(alice, bob)]
   return s.count(1), s.count(-1)
    

a0, a1, a2 = input().strip().split(' ')
alice = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
bob = [int(b0), int(b1), int(b2)]

result = solve(alice, bob)
print (" ".join(map(str, result)))