'''
Find all 0-9-pandigital numbers where:
    d2d3d4 % 2 = 0
    d3d4d5 % 3 = 0
    ...
    d8d9d10 % 17 = 0
'''
import itertools

def is_pan(num):
    '''
    Check if a number is 0-9-pandigital.
    However, checking every number is way too slow.
    '''
    ordered = "0123456789"
    return "".join(sorted(str(num))) == ordered

def sub_diff(num):
    '''
    Return True if the number meets the criterion.
    '''
    #! not quite
    primes = [1, 2, 3, 5, 7, 11, 13, 17]

    for i, prime in enumerate(primes):
        sub_num = int(str(num)[i:i+3])
        if sub_num % prime != 0:
             return False
        i += 1

    return True

total = 0

for item in itertools.permutations("1234567890", 10):
    test = int("".join(item))
    if sub_diff(test):
        total += test

print total
