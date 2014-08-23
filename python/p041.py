'''
Find the largest pandigital prime.

The sum of 8 and 9-digit pandigital numbers divides by three,
so all the numbers do too and none are prime.

Start with the biggest pandigital 7-digit number and work down.

You could also create the pandigital numbers using combinatorics.
'''
from utils import is_pandigital, is_prime
i = 7654321

while True:
    if is_pandigital(i):
        if is_prime(i):
            break
    i -= 2

print i
