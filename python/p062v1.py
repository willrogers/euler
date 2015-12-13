import math
import sys
import collections
import itertools


TARGET = 3


def search_for_permutations(numbers, target):
    """Find numbers that are permutations of each other."""
    ncopy = numbers[:]
    while ncopy:
        n = ncopy.pop()
        perms = [n]
        ps = itertools.permutations(list(str(n)))
        ps = [int(''.join(p)) for p in ps]
        for poss in ncopy:
            if poss in ps:
                ncopy.remove(poss)
                perms.append(poss)
            if len(perms) == target:
                return perms
    return []


if __name__ == '__main__':
    i = 1
    current_length = 1
    cubes = collections.defaultdict(list)

    while True:
        c = i ** 3
        clength = int(math.log10(c)) + 1
        print(clength)
        if clength > current_length:
            print(cubes[current_length])
            perms = search_for_permutations(cubes[current_length], TARGET)
            if perms:
                print(perms)
                sys.exit()
            current_length = clength
        cubes[clength].append(c)
        i += 1

