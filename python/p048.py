"""
Find the last 10 digits of 1^1 + 2^2 + ... + 1000^1000

The trick here is that you can always forget the leading digits because 
they won't contribute to the sum.
"""
def pow10to10(x, y):
    """
    Get the power, but each time truncate to 10^10 so that the numbers
    never overflow.
    """
    tot = 1
    for i in range(y):
        tot = (tot * x) % 10000000000
    return tot

tot = 0
for i in range(1, 1001):
    tot = tot + pow10to10(i, i)

print(tot) 
