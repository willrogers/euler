'''
Find the longest string of consecutive primes which sum to another prime
below 1m.
'''
from utils import is_prime
import itertools

UPPER = 1000000

ps = [2]

# generate plenty of primes
for i in range(3, 5000, 2):
    if is_prime(i):
        ps.append(i)

found = []

# i is the length of sequence we're currently trying
# work from the longest sequences
for i in range(len(ps)+1, 0, -1):
    print "i =", i
    # j is the starting index for each sum required in a loop through the array
    for j in range(len(ps)-i+1):
        # k is the items being summed in this particular attempt
        attempt = [ps[k+j] for k in range(i)]
        tot = sum(attempt)
        # is this sum prime?
        if is_prime(tot):
            print tot
            # if so, is it less than the limit?
            if tot < UPPER:
                found = attempt
                break
    # interesting - no easy way to break multiple loops
    if found:
        print "breaking"
        print found
        print sum(found)
        print len(found)
        break

