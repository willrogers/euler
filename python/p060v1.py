'''
This is too slow - more than two minutes even using pypy.
'''

from itertools import combinations, permutations, product
from utils import prime_gen, is_prime

# Deduce from trial and error that 10000 primes are needed
primes = list(prime_gen(10000))


def prime_perms(tup):
    '''
    Given a tuple of numbers, return True if all permutations of two of 
    those numbers are prime.
    '''
    perms = permutations(tup, 2)
    perms = [int(''.join(str(i) for i in p)) for p in perms]
    return all(is_prime(p) for p in perms)


dups = [sorted(x) for x in combinations(primes, 2) if prime_perms(x)]

def extend(tups, primes):
    '''
    Return a list of tuples formed by adding primes to existing tuples
    which combine to make prime numbers.
    '''
    longer_tups = []
    for t in tups:
        for p in primes:
            # The last in the sequence is the largest prime.
            if p < t[-1]:
                continue
            ok = True
            for tp in t:
                if not is_prime(int(str(tp) + str(p))) or not is_prime(int(str(p) + str(tp))):
                    ok = False
                    break
            if ok:
                longer_tups.append(t + [p,])

    return longer_tups

trips = extend(dups, primes)
quads = extend(trips, primes)
quins = extend(quads, primes)

print(min(sum(q) for q in quads))

