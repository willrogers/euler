'''
Find the first four consecutive numbers each to have four distinct prime
factors.
'''
from utils import factors
import itertools

LEN = 4
START = 0
COUNT = 0

for i in itertools.count():
    facs = factors(i)
    if len(set(facs)) >= LEN:
        COUNT += 1
        if not START:
            START = i
    else:
        COUNT = 0
        START = 0

    if COUNT == LEN:
        print START
        break


