'''
Find the smallest number x such that 2x, ... 6x contain the same 
digits.
'''
import sys
import itertools

MULT = 6

def digits(n):
    return sorted(str(n))

for i in itertools.count(1):
    digs = digits(i)
    matched = True
    for j in range(1, MULT+1):
        if digits(i*j) != digs:
            matched = False
            break
    if matched:
        print i
        break
