'''
Check for all numbers below 1m which are palindromic both
as decimal and binary numbers.

I use string manipulation for palindromes - it seems to work
quite well.
'''
from utils import is_palindrome

LIMIT = 1000000
total = 0 

for i in range(LIMIT):
    if is_palindrome(i):
        bins =  bin(i)
        # remove '0b' from the string
        if is_palindrome(bins[2:]):
            print i
            print bins
            total += i

print total

