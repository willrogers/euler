'''
This is too slow - more than two minutes even using pypy.
'''

from itertools import combinations, permutations
from utils import prime_gen, is_prime

# Deduce from trial and error that primes up to 10000 are needed
primes = list(prime_gen(10000))
print(len(primes))


# There are 14m calls to is_prime, meaning that it must be 
# called multiple times on the same number.  Quicker to cache
# results and only call it on new numbers.
prime_cache = {}

def is_prime_cached(n):
    try:
        return prime_cache[n]
    except KeyError:
        p = is_prime(n)
        prime_cache[n] = p
        return p


def prime_perms(tup):
    '''
    Given a tuple of numbers, return True if all permutations of two of 
    those numbers are prime.
    '''
    perms = permutations(tup, 2)
    perms = [int(''.join(str(i) for i in p)) for p in perms]
    return all(is_prime_cached(p) for p in perms)


def extend(tups, primes):
    '''
    Return a list of tuples formed by adding primes to existing tuples
    which combine to make prime numbers.
    '''
    longer_tups = []
    for t in tups:
        for p in primes:
            # The last in the sequence is the largest prime.
            if p <= t[-1]:
                continue
            ok = True
            for tp in t:
                if not is_prime_cached(int(str(tp) + str(p))) or not is_prime_cached(int(str(p) + str(tp))):
                    ok = False
                    break
            if ok:
                longer_tups.append(t + [p,])

    return longer_tups

dups = [sorted(x) for x in combinations(primes, 2) if prime_perms(x)]
print len(dups)
trips = extend(dups, primes)
print len(trips)
quads = extend(trips, primes)
print len(quads)
quins = extend(quads, primes)
print len(quins)

print(min(sum(q) for q in quins))

