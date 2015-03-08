"""
The numbers going out diagonally from the centre are in arithmetic
sequence:

1,3,13,31,... 4n^2 - 10n + 7
1,5,17,37,... 4n^2 - 8n + 5
1,7,21,43,... 4n^2 - 6n + 3
1,9,25,49,... 4n^2 - 4n + 1

We need the sum of primes of the set containing these sequences
of equal length.
"""
from itertools import izip
from utils import is_prime


def gen_sequence(a, b, c):
    """
    Generate a sequence of quadratic polynomials with
    the specified coefficients.
    """
    i = 1
    while True:
        yield a * i**2 + b * i + c
        i += 1


if __name__ == '__main__':
    primes = 0
    diag_numbers = set()
    for i, new_nums in enumerate(izip(gen_sequence(4, -10, 7),
                        gen_sequence(4, -8, 5),
                        gen_sequence(4, -6, 3),
                        gen_sequence(4, -4, 1))):
        diag_numbers.update(new_nums)
        primes += len([n for n in new_nums if is_prime(n)])
        frac = primes*1.0 / len(diag_numbers)
        if i > 0 and frac < 0.1:
            break

    # i is the centre of the square to the edge. We need the
    # full size.
    print(2*(i-1)+1)




