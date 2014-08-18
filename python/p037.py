'''
Find the sum of all 11 truncatable primes (that is, both ways).
Single-digit primes don't count.
'''
from utils import is_prime
import itertools

TOTAL = 11

def truncatable(p):
    s = str(p)
    l = len(s)
    for i in range(1, l):
        if not is_prime(int(s[i:])):
            return False
        if not is_prime(int(s[:i])):
            return False
    return True

truncs = []
for i in itertools.count(11, 2):
    if is_prime(i):
        if truncatable(i):
            truncs.append(i)
    if len(truncs) == TOTAL:
        break

print sum(truncs)


