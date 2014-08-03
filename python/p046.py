'''
What is the smallest odd composite that cannot be written as the sum
of a prime and twice a square?
'''

from utils import is_prime, EPS, is_square
import itertools

PRIMES = []

def refutes(i):
    for p in PRIMES:
        if is_square((i - p) / 2):
            return False
    return True

for i in itertools.count(3, 2):
    if is_prime(i):
        PRIMES.append(i)
    else:
        if refutes(i):
            print("%s refutes" % i)
            break
        

