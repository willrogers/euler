
from utils import int_reverse, int_reverse2

ODDS = ['1', '3', '5', '7', '9']
LIMIT = 1000


def all_odd(n):
    for digit in str(n):
        if not digit in ODDS:
            return False
    return True


def reversible(n):
    if n % 10 == 0:
        return False
    ans = n + int_reverse2(n)
    return all_odd(ans)

tot = 0

for i in xrange(LIMIT):
    if reversible(i):
        print i
        tot += 1

print
print(tot)

