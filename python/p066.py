# Diophantine equations.
# x^2 - Dy^2 = 1
# Find the minimal value of x for which there is a solution for different values of D.

# There are no solutions if D is square.

import math


def is_square(n):
    root = math.sqrt(n)
    return int(root) == root


def find_min_x(D):
    for x in xrange(2, 10000000):
        xs = x**2
        if xs % D == 1:
            target = (xs - 1)/D
            root = math.sqrt(target)
            if root == int(root):
                if (xs - D * target) == 1:
                    return x


results = {}
target = 75

for D in range(target):
    if not is_square(D):
        min_x = find_min_x(D)
        print('Min x for {0} is {1}'.format(D, min_x))
        results[D] = min_x


print('Max X for D up to {0} is {1}'.format(target, max(results.values())))






