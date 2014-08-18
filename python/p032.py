'''
Find all the products whose two multiplicands and 
product contain the digits 1-9 exactly once.
Example: 39 * 186 = 7254

Multiplicands must have no more than four digits.
If one has four, the other may not have more than 1.
'''

from utils import is_pandigital

# we only want unique products, and some are duplicated
prods = set()
for i in range(10000):
    for j in range(1000):
        k = i * j
        if k < 100000:
            s = str(k) + str(i) + str(j)
            if is_pandigital(s):
                prods.add(int(k))

print sum(prods)

