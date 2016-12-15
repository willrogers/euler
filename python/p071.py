"""
Find the numerator of the reduced proper fraction closest below
3/7 with denominator <= 1000000.

Just find the closest fraction for each denominator then find the
closest of all.
"""
from __future__ import division
import math

LIMIT = 1000000
max_tuple = ()
max = 0

for d in xrange(LIMIT):
    n = math.floor(3 * d / 7)
    if n > max and n / d < 3 / 7:
        max = n
        max_tuple = (int(n), d)
    
# It turns out the answer doesn't need simplifying.
print(max_tuple[0])
