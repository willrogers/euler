# Find the highest prime factor of a composite number.

import sys
import math 

LIMIT = 600851475143

factors = []

# Just get the next smallest factor
def get_next_factor(n):
    i = 2
    if i == n:
        return -1
    while True:
        if n % i == 0:
            return i
        i += 1


latest = LIMIT
while True:
    x = get_next_factor(latest)
    factors.append(x)
    # divide the number by the latest factor
    latest = latest / x
    # if we get the same factor, it's prime
    if latest == 1:
        break

print factors[-1]

