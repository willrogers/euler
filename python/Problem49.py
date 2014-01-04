'''
There are two arithmetic sequences which create three four-digit primes
x whose terms are permutations of each other.
1487, 4817, 8147 is one.  What is the other?
'''

from utils import is_prime

LOWER = 1001
UPPER = 10000

PRIMES = []
POSSIBLES = []

for i in range(LOWER, UPPER, 2):
    if is_prime(i):
        PRIMES.append(i)

    
# this part takes the time
for p in PRIMES:
    limit = ((UPPER - p)/2)
    for i in range(2, limit, 2):
        p1 = p + i
        p2 = p + 2 * i
        if p1 in PRIMES and p2 in PRIMES:
            POSSIBLES.append((p, p1, p2))


for poss in POSSIBLES:
    if sorted(str(poss[0])) == sorted(str(poss[1])) == sorted(str(poss[2])):
        print poss


