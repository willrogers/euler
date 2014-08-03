
'''
https://projecteuler.net/problem=113

How many numbers below a googol are not bouncy?  See also problem 112.

This still takes 2m to get to 10 ** 10.
'''

import math
from utils import is_bouncy


#LIMIT = 10 ** 100
LIMIT = 10 ** 5

nb = 0

# we don't have time to check each number

i = 1

while i < LIMIT:
    length = int(math.floor(math.log10(i)))
    for j in range(3, length + 1):
        if i > 10 ** j:
            prefix = int(str(i)[0:j])
            if is_bouncy(prefix):
                num = 10 ** (len(str(i)) - j)
#                print "skipping from", i,
                i = ((i + num) / num) * num
#                print "to ", i
    '''
        if i > 10 ** 4:
            prefix = int(str(i)[0:4])
            if is_bouncy(prefix):
                num = 10 ** (len(str(i)) - 4)
                print "skipping from", i,
                i = ((i + num) / num) * num
                print "to ", i
        if i > 10 ** 5:
            prefix = int(str(i)[0:5])
            if is_bouncy(prefix):
                num = 10 ** (len(str(i)) - 5)
                print "skipping from", i,
                i = ((i + num) / num) * num
                print "to ", i
        if i > 10 ** 6:
            prefix = int(str(i)[0:6])
            if is_bouncy(prefix):
                num = 10 ** (len(str(i)) - 6)
                print "skipping from", i,
                i = ((i + num) / num) * num
                print "to ", i
        if i > 10 ** 7:
            prefix = int(str(i)[0:7])
            if is_bouncy(prefix):
                num = 10 ** (len(str(i)) - 7)
                print "skipping from", i,
                i = ((i + num) / num) * num
                print "to ", i
    '''
    if not is_bouncy(i):
        nb += 1

    if i % 1000000 == 0:
        print("got to ", i)

    i += 1


print(nb)
