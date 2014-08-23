"""
Find the last 10 digits of 1^1 + 2^2 + ... + 1000^1000

The trick here is that you can always forget the leading digits because
they won't contribute to the sum.
"""
LIMIT = 1000

def pow10to10(x, y):
    """
    Get the power, but each time truncate to 10^10 so that the numbers
    never overflow.
    """
    tot = 1
    for i in range(y):
        tot = (tot * x) % int(1e10)
    return tot

tot = sum(pow10to10(i+1, i+1) for i in range(LIMIT))

print tot % int(1e10)
