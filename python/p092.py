"""
Square digit chains.
"""
from __future__ import division


LIMIT = int(1e7)


def next_str(previous):
    return sum(int(c)**2 for c in str(previous))


def next_math(previous):
    square_sum = 0
    while previous > 0:
        square_sum = square_sum + (previous % 10) ** 2
        previous //= 10
    return square_sum


if __name__ == '__main__':
    tot = 0
    cache = {1:1, 89:89}
    for i in xrange(1, LIMIT):
        temp = i
        while temp not in cache:
            temp = next_math(temp)
        temp = cache[temp]
        cache[i] = temp
        if temp == 89:
            tot += 1

    print(tot)
