'''
There are two arithmetic sequences which create three four-digit primes
x whose terms are permutations of each other.
1487, 4817, 8147 is one.  What is the other?
'''

from utils import is_prime

LOWER = 1001
UPPER = 10000

PRIMES = []
answers = []

for i in range(LOWER, UPPER, 2):
    if is_prime(i):
        PRIMES.append(i)


def int_anagram(int1, int2):
    return sorted(str(int1)) == sorted(str(int2))


for p in PRIMES:
    limit = ((UPPER - p)/2)
    for i in range(2, limit, 2):
        p1 = p + i
        p2 = p + 2 * i
        if not int_anagram(p, p1) or not int_anagram(p, p2):
            continue
        if p1 in PRIMES and p2 in PRIMES:
            answers.append((p, p1, p2))


ANSWER1 = (1487, 4817, 8147)
for answer in answers:
    if answer != ANSWER1:
        print "".join(str(a) for a in answer)

