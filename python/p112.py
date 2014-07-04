'''
https://projecteuler.net/problem=112
What's the lowest number for which the proportion of 'bouncy' numbers
is exactly 99%?
'''

from utils import is_bouncy

bouncy = 0
i = 1

while True:
    b = is_bouncy(i)
    if b:
        bouncy += 1

    f = float(bouncy)/ i
    if f == 0.99:
        print f, i, bouncy
        break

    i += 1

