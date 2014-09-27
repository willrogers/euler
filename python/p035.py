"""
How many circular primes are there below 1m?
A circluar prime has all rotations of the number as also prime.

This version may be inefficient, but it solved it in about 7s.
"""

import math
from utils import is_prime, prime_gen, srotate

THRESHOLD = 1000000

primes = prime_gen(THRESHOLD)

cps = []

for prime in primes:
    rotations = srotate(prime)
    if all(is_prime(rot) for rot in rotations):
        cps.append(prime)

print len(cps)
