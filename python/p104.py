
# https://projecteuler.net/problem=104

# It seems a bit lucky that you don't have to find a billion
# fibonacci numbers with pandigital ends before you find one
# with a pandigital start.


F0 = 0
F1 = 1
F2 = 1

INTS = set(range(1, 10))

BILLION = 1000000000


def pan_end(n):
    '''
    Return True if the last nine digits are 1-9 pandigital.
    '''
    # using strings is slower than calculating
    #end = str(n)[-9:]
    end = str(n % BILLION)
    return pan_str(end)

def pan_start(n):
    '''
    Return True if the first nine digits are 1-9 pandigital.
    '''
    start = str(n)[:9]
    return pan_str(start)

def pan_str(nstr):
    ints = set(int(digit) for digit in nstr)
    return ints == INTS


last_but_one = 0
last = 1
n = 2
while True:
    fib = last_but_one + last
    last_but_one = last
    last = fib
    if pan_end(fib):
        if pan_start(fib):
            print n
            break

    n += 1



