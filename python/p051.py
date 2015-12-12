import sys
import utils
import itertools

BASE = 10
TARGET = 7


def all_combs(seq):
    combs = []
    for i in range(1, len(seq) + 1):
        combs.extend(itertools.combinations(seq, i))
    return combs


def test_family(number, length, digits):
    not_prime = 0
    primes = []
    for i in range(BASE):
        replaced = utils.int_replace_all(number, length, digits, i)
        if utils.is_prime_cached(replaced):
            primes.append(replaced)
        else:
            not_prime += 1
        if not_prime >= BASE - TARGET:
            return []
    return primes


def handle_one_length(length):
    poss = all_combs(range(length))
    full = range(length)
    start = int(10 ** (length - 1))
    for p in poss:
        missing = [f for f in full if f not in p]
        for m in missing:
            for i in range(1, BASE ** len(missing)):
                fam_start = utils.int_replace(start, length, missing, i)
                t = test_family(fam_start, length, p)
                if t and len(str(t[0])) == len(str(t[-1])):
                    return t


length = 0
done = False
while not done:
    t = handle_one_length(length)
    if t is not None:
        print(min(t))
        done = True
    length += 1
