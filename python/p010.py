# Find the sum of all the primes below two million.
import math
import utils
import numpy

LIMIT = 2000000


def naive():
    total = 2
    for i in range(3, LIMIT, 2):
        if utils.is_prime(i):
            total += i
    return total


def dict_cancel():
    poss = range(2, LIMIT)
    prime = {i: True for i in range(2, LIMIT)}
    for i in [2] + range(3, LIMIT, 2):
        count = i * 2
        while count < LIMIT:
            prime[count] = False
            count += i

    total = sum(x for x in prime.keys() if prime[x])
    return total


def array_cancel():
    a = numpy.arange(LIMIT)
    a[1] = 0
    for i in [2] + range(3, LIMIT, 2):
        count = i * 2
        while count < LIMIT:
            a[count] = 0
            count += i

    total = sum(a)
    return total


print(dict_cancel())

