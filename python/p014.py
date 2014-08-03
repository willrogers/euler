'''
Find the longest chain starting below a million where:
if n is even, n = n / 2
if n is odd,  n = 3n + 1
and stopping at 1.

First attempt, after removing print statements and unnecessary function
calls, took about a minute.
'''

import cProfile

def shrink(n):
    return n / 2

def grow(n):
    return 3 * n + 1

def reduce(n):
    l = []
    while n != 1:
        l.append(n)
        if n % 2 == 0:
#            n = shrink(n)
            n = n / 2
        else:
            n = grow(n)
    l.append(1)
#    print l
    return len(l)

def sreduce(n):
    l = 0
    while n != 1:
        l += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    l += 1
    return l


def run():
    max = (0,0)
    for i in range(1, 1000000):
        j = sreduce(i)
        if j > max[1]:
            max = (i,j)
    print(max[0])
    
run()
