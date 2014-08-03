"""
What's the millionth lexicographic permutation of 0123456789?

Admittedly, this is a bit of a cheat...
"""

from itertools import permutations, islice

N = 1000000
digits = [0,1,2,3,4,5,6,7,8,9]

i = 1
for i, item in enumerate(permutations(digits)):
    if i == N-1:
        print("".join(str(x) for x in item))
        break


# Use islice to create a subset of an iterator
#print next(islice(permutations(digits), N-1, N))
