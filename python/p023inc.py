"""
Find the sum of all the positive integers which cannot be written as the 
sum of two abundant numbers.

We know the highest such number is less than 28123.

I think this now works, but is too slow.  It takes half a second to check up
to 1000.

Version 2 completed in about 2 minutes, which is still really too slow.  
The divisors function takes a bit less than half, so there is optimisation 
in the rest as well.
"""

from utils import divisors

LIMIT = 28123

def abundant(n):
    d = divisors(n)
    s = sum(d)
    return s > n

abuns = []

for i in range(LIMIT):
    if abundant(i):
        abuns.append(i)

print(len(abuns))

combs = []
# I think this is now the slow part.
for i in abuns:
    for j in abuns:
        if i+j < LIMIT:
            combs.append(i+j)
        else:
            break

print("size combs = ", len(combs))
scombs = set(combs)

print("size scombs = ", len(scombs))
total = 0
for i in range(LIMIT):
    if i not in combs:
        total += i

# Before, I checked every number by checking abuns twice.
# This was slow.

print(total)
