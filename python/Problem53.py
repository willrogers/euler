'''
How many values of nCr, 1<=n<=100 are greater than 1m?
'''

from utils import factorial

LIMIT = 1000000

total = 0

def ncr(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

for n in range(1, 101):
    print n
    for r in range(n):
        if ncr(n, r) > LIMIT:
            print n, r
            total += 1

    
print total
