'''
Find the longest string of consecutive primes which sum to another prime
below 1m.
'''
from utils import is_prime, prime_gen
import itertools

UPPER = 1e6

# generate plenty of primes
ps = [p for p in prime_gen(5000)]

found = []

# i is the length of sequence we're currently trying
# work from the longest sequences
for i in range(len(ps)+1, 0, -1):
    # j is the starting index for each sum required in a loop
    # through the array
    for j in range(len(ps)-i+1):
        # k is the items being summed in this particular attempt
        attempt = [ps[k+j] for k in range(i)]
        tot = sum(attempt)
        # is this sum prime?
        if is_prime(tot):
            # if so, is it less than the limit?
            if tot < UPPER:
                found = attempt
                break
    # interesting - no easy way to break multiple loops
    if found:
        print sum(found)
        break

