#!/usr/bin/env python
"""
How many circular primes are there below 1m?
A circluar prime has all rotations of the number as also prime.

This version must be inefficient, but it solved it in about 20s.
"""

import math
from utils import is_prime, srotate

threshold = 1000000
primes = []

tot = 0
for i in range(1, threshold, 2):
    if is_prime(i):
#        print i
        primes.append(i)
        tot += 1

cps = []

for prime in primes:
    rotations = srotate(prime)
    cp = True
    for rot in rotations:
        if not is_prime(rot):
            cp = False
            break
    if cp:
        cps.append(prime)    

print cps
print len(cps)
