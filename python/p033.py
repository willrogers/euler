from __future__ import division
from fractions import Fraction
import operator

def simplify(x, y):
    """
    Use incorrect cancelling to remove any matching digits on the top
    or bottom of the fraction.

    If the cancelling fails, return None
    """
    dig1 = x // 10
    dig2 = x % 10
    dig3 = y // 10
    dig4 = y % 10
    # discount 'trivial' cancellations
    if dig2 == 0 or dig4 == 0:
        return None
    if dig1 == dig3:
        return dig2, dig4
    elif dig1 == dig4:
        return dig2, dig3
    elif dig2 == dig3:
        return dig1, dig4
    elif dig2 == dig4:
        return dig1, dig3
    
    return None


answers = []

for num in range(10, 100):
    # fraction < 1 => denom > num
    for denom in range(num, 100):
        res = simplify(num, denom) 
        if res is not None:
            f = Fraction(num, denom)
            g = Fraction(*res)
            if f == g:
                answers.append(Fraction(num, denom))

f = reduce(operator.mul, answers)
print f.denominator
