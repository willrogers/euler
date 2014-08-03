"""
Amicable pairs are numbers whose sums of divisors are equal to the other number.

How many are there below 10000?

This is a fairly naive attempt, which took 10s. The divisors method is slow.
"""

from utils import divisors

limit = 10000

sds = {}
aps = []

for i in range(limit):
    sd = sum(divisors(i))
    sds[i] = sd


for item in sds.keys():
    try:
        if sds[sds[item]] == item and item != sds[item]:
            aps.append(item)
    except KeyError: # The sum may be bigger than the numbers in the dict
        pass

print sum(aps)
