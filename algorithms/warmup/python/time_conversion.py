#!/bin/python3

import sys, time

s = input().strip()
t = time.strptime(s,'%I:%M:%S%p')
print(time.strftime('%H:%M:%S', t))
