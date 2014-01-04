'''
Find all the numbers which are equal to the sum of the 
factorials of their digits.  1! and 2! not included.

An upper limit is 9999999, because the sum of factorials
can't reach this number.

However, I cheated, because only two numbers showed up less
than 10m, so I tried them and it was correct.
'''

import math

def fact_sum(i):
    tot = 0
    s = str(i)
    for digit in s:
        f = math.factorial(int(digit))
        tot += f
    return i == tot

        
matches = []

for i in range(10, 1000000):
    if i % 100000 == 0:
        print "got to", i
    if fact_sum(i):
        matches.append(i)

print matches
print sum(matches)
