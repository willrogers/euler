'''
This is still quite slow - around 10 seconds using pypy.
'''

from itertools import combinations, permutations
from utils import prime_gen, is_prime
import math

# Deduce from trial and error that primes up to 10000 are needed
primes = list(prime_gen(10000))


# There are typically 14m calls to is_prime, meaning that it must be 
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


def prime_test(p1, p2):
    # This mathematical manipulation is slightly quicker
    # than the string manipulation I'd often do.
    test1 = p1*10**int(math.ceil(math.log10(p2))) + p2
    if not is_prime_cached(test1):
        return False
    test2 = p2*10**int(math.ceil(math.log10(p1))) + p1
    return is_prime_cached(test2)
    

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
                if not prime_test(tp, p):
                    ok = False
                    break
            if ok:
                longer_tups.append(t + [p,])

    return longer_tups

dups = [sorted(x) for x in combinations(primes, 2) if prime_test(*x)]
trips = extend(dups, primes)
quads = extend(trips, primes)
quins = extend(quads, primes)

print(min(sum(q) for q in quins))
