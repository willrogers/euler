'''
Find d < 1000 for which 1/d has the longest recurring cycle in 
its decimal.
'''
from decimal import Decimal, getcontext

MAX_DIVISOR = 1000
# Arithmetic precision needs to be 2000 to find a repetition of up
# to length 1000
PRECISION = 2000
# How many leading digits we try removing to look for repetition
MAX_PREFIX = 5

getcontext().prec = PRECISION

def get_recurrence(s):
    '''Find the length of the shortest repetition in a sequence.'''
    for i in range(1, len(s)):
        if s[i:].startswith(s[:i]):
            return(i) 

def find_recurrence(d, leading_digits):
    '''
    Given a number, try to find the length of any recurrence.
    '''
    try:
        s = str(d).split('.')[1]
    except IndexError: #integer
        print(d)
        return 0
    # recurrence in a decimal may not start with the leading digit
    tries = [s[i:] for i in range(leading_digits)]
    rec = max(get_recurrence(go) for go in tries)
    return rec
    

max_recurrence = 0
value = 0 
for i in range(2, MAX_DIVISOR):
    result = Decimal(1) / Decimal(i)
    length = 0
    try:
        length = find_recurrence(result, MAX_PREFIX)
    except IndexError: # integer
        pass
    if length > max_recurrence:
        max_recurrence = length
        value = i 

print(value)
