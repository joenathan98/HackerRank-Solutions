#!/bin/python3

import sys

def sums(n,d):
    return d*(((n//d)*((n//d)+1))//2)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sums(n-1,3) + sums(n-1,5) - sums(n-1,15))
