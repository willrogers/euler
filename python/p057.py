
from fractions import Fraction

SAMPLES = 1001
ZERO = Fraction(0,1)


def est_generator(limit=1000):
    """
    The estimation is 1 plus an iterating sequence.
    Improve the estimation by adding 2 to the last guess
    then inverting. Add 1 before returning each value.
    """
    last_guess = ZERO
    for i in range(limit):
        yield 1 + last_guess
        denom = last_guess + 2
        last_guess = 1 / denom


def longer_int(int1, int2):
    """
    Return True if int1 has more digits than int2.
    """
    return len(str(int1)) > len(str(int2))


if __name__ == '__main__':
    total = 0
    for f in est_generator(SAMPLES):
        if longer_int(f.numerator, f.denominator):
            total += 1
    print(total)

