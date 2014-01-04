"""
http://projecteuler.net/problem=12

What's the first triangle number to have over 500 divisors?
Version 1: 4s to get to 100 divisors, > 1m for 200.  Too slow.
Version 2: Tried trying doubling i, but got a memory error.  
Not sure why.
"""

from utils import triangle, is_prime

def factors(a):
    fs = []
    i = 2
    while i <= a:
        if a % i == 0:
            fs.append(i)
            a = a / i
        else:
            i += 1
    return fs


def combs(lst, agg):
    print "list: ", lst
    if len(lst) == 1:
        return agg.append(lst[0])
    else:
        last = lst.pop()
        print last
        return agg.extend(combs( [ last * item for item in lst ] ))

def divisors(a):
    fs = factors(a)
    return combs(fs, [])



test = [2, 5, 10, 20, 24]

for item in test:
    print "Testing ", item
    print "For %s, %s divisors" % (item, len(divisors(item)))

# There's no point checking every triangle number.
# This doubles i until we reach the threshold
