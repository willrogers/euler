"""
Find the one Pythagorean triplet for which a + b + c = 1000.
http://projecteuler.net/problem=9

Very simplistic.  Doesn't exclude duplicates, but gets the answer quick enough.
"""

import math

triplets = []
for i in range(1, 1000):
    for j in range(1, 1000):
        if i + j >= 1000:
            continue
        else:  
            k = 1000 - i - j
            tri = sorted([i, j, k])
            triplets.append(tri)

def is_pythagorean(triplet):
    l = list(triplet)
    ls = sorted(l)
    sq1 = ls[0] * ls[0] + ls[1] * ls[1]
    sq2 = ls[2] * ls[2]
    return sq1 == sq2


for triplet in triplets:
    if is_pythagorean(triplet):
        print triplet[0] * triplet[1] * triplet[2]
        break

