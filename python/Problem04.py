# Find the largest palindrome made from the product of two 
# three-digit numbers.
# http://projecteuler.net/problem=4
# Version 1: about 1 second, though it's very inefficient.

from utils import is_palindrome


to_test = [1, 5, 12, 15, 22, 2352, 2332, 45654]

for item in to_test:
    print "Item %s, palindromic: %s" % (item, is_palindrome(item))

# Simple-minded: just get all the products of 3-digit integers.
products = []

for i in range(100, 1000):
    for j in range(100, 1000):
        n = i * j
        products.append(n)

# Sort and reverse so we look at the biggest ones first.
products = sorted(products)
products.reverse()


# Check for the first palindrome.
for item in products:
    if is_palindrome(item):
        print item
        break
