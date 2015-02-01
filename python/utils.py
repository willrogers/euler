import os
import math
import itertools

EPS = 0.00000001
DATADIR = '../data'


def from_file(filepath):
    """
    Return the content of a file as a string, including newlines.
    """
    with open(filepath) as file:
        lines = file.readlines()
        content = ''.join(lines)
    return content.strip()


def load_data(filename):
    here = os.path.dirname(os.path.realpath(__file__))
    datafile = os.path.join(here, DATADIR, filename)
    return from_file(datafile)


def divisors(n):
    """
    Return all the divisors of an integer.  Does not include the number
    itself.
    """
    divs = []
    for i in range(1, n / 2 + 1):
        if n % i == 0:
            divs.append(i)
    return divs


def divisors2(n):
    """
    Return all the divisors of an integer.  Does not include the number
    itself.
    This is quicker than divisors because it's much quicker to factorise
    than to check every number to see if it divides.
    """
    f = factors(n)
    d = []
    # Now build all possible divisors from the factors.
    for i in range(len(f)):
        c = itertools.combinations(f, i)
        for comb in c:
            # product of combination
            d.append(reduce(lambda x,y: x*y, comb, 1))
    # only want unique values
    return sorted(list(set(d)))


def factors(n):
    """
    Return all the factors of n as a list.
    """
    fs = []
    i = 2
    while n > 1:
        if n % i == 0:
            fs.append(i)
            n = n / i
        else:
            i += 1
    return fs


def pow(x, n):
    """
    Return x to the power n.
    """
    total = 1
    for i in range(1, n + 1):
        total = x*total
    return total


def is_prime(n):
    """
    Return True if an integer is prime.
    """
    if n < 2:
        return False
    max = int(math.sqrt(n)) + 1
    for i in range(2,max):
        if n % i == 0:
            return False
    return True


def prime_gen(n):
    yield 2
    x = 3
    while x < n:
        if is_prime(x):
            yield x
        x += 2


def pentagons():
    i = 0
    while True:
        i += 1
        yield i * (3 * i - 1) / 2


def is_pen(num):
    '''
    Only the positive solution is valid.
    '''
    n = (1 + math.sqrt(1 + 24 * num)) / 6.0
    nround = round(n, 0)
    return abs(n - nround) < EPS


def triangles():
    start = 0
    for i in itertools.count(start):
        yield i * (i + 1) / 2


def hexagons():
    start = 0
    for i in itertools.count(start):
        yield i * (2 * i - 1)


def is_tri(num):
    n = (-1 + math.sqrt(1 + 8*num)) / 2.0
    nround = round(n, 0)
    return abs(n-nround) < EPS


def is_hex(num):
    n = (1 + math.sqrt(1 + 8*num)) / 4.0
    nround = round(n, 0)
    return abs(n-nround) < EPS


def triangle(n):
    """
    Return the nth triangle number.
    """
    tot = 0
    for i in range(n):
        tot += i + 1
    return tot


def triangle2(n):
    """
    Return the nth triangle number.
    """
    return 0.5 * n * (n + 1) 


def is_triangle(n):
    """
    Invert the formula t = 1/2 * n * (n+1)
    """
    root = math.sqrt(0.25 + 2 * n)
    epsilon = 0.0000001
    n  = root - 0.5
    return abs(round(n) - n)  < epsilon    


def is_square(i):
    x = math.sqrt(i)
    y = round(x, 0)
    return abs(x - y) < EPS


def is_palindrome(n):
    """
    Checks if an integer is palindromic.  I don't know if this string 
    manipulation is efficient.
    """
    s = str(n)
    l = len(s)
    for i in range(l / 2):   
        if s[i] != s[l - i- 1]:
            return False
    return True


def int_reverse(n):
    return int(''.join(x for x in reversed(str(n))))
def int_reverse2(n):
    new = n % 10
    for i in range(int(math.ceil(math.log10(n)))):
        new *= 10 + n % 10
        n /= 10
    #print new
    return int(''.join(x for x in reversed(str(n))))


def is_pandigital(i):
    '''
    Return True if the integer contains each digit once up to the
    number of digits in i.
    '''
    s = str(i)
    if '0' in s:
        return False
    n = len(s)
    if n < 1 or n > 9:
        return False 
    digits = [str(num) for num in range(1, n+1)]
    ss = sorted(s)
    if ss == digits:
        return True
    return False


def rotate(n):
    """
    Provide all rotations of an integer.  For example:
    314 -> [314, 143, 431]
    See also srotate.
    """
    mag = math.trunc(math.log10(n))
    rotations = [n]
    for i in range(mag):
        x = n % 10
        y = (n - x) / 10
        z = pow(10,mag) * x + y
        rotations.append(z)
        n = z

    return rotations


def srotate(n):
    """
    Provide all rotations of an integer.  For example:
    314 -> [314, 143, 431]
    Interestingly, I found srotate to take about 2/3 the time of rotate.
    """
    rotations = []
    s = str(n)
    for letter in s:
        t = s[1:] + letter
        rotations.append(int(t))
        s = t
    return rotations


def factorial(n):
    assert n >= 0
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def is_bouncy(n):
    '''
    See 112 and 113.
    '''
    not_forward = False
    not_back = False
    last = 0
    for i in str(n):
        if int(i) >= last:
            last = int(i)
        else:
            not_forward = True
            break

    last = 0
    for i in reversed(str(n)):
        if int(i) >= last:
            last = int(i)
        else:
            not_back = True
            break

    return not_forward and not_back

