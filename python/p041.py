'''
Find the largest pandigital prime.

To start with, assume that it has 9 digits.

NO!  Just work down from the top and find the first one!
That didn't work, either.

7652413 was the biggest - then they seemed to stop very abruptly.
Is there a logical reason for this?
Yes.  The sum of 8 and 9-digit pandigital numbers divides by three,
so the numbers do too.

You could also create the pandigital numbers using combinatorics.
'''
from utils import is_pandigital, is_prime
i = 7654321
pan_primes = []

while True:
    if is_pandigital(i):
        if is_prime(i):
            print(i, "is prime")
            exit()
    i -= 2

print(pan_primes)
