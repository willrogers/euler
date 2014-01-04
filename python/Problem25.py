"""
Find the first term in the fibonacci sequence which has 1000 digits.
"""

fiblen = 1000

n = 1
fibn = 1
fibnp1 = 1
while True:
    fibnp2 = fibn + fibnp1
    # now reassign for n+1
    n += 1
    fibn = fibnp1
    fibnp1 = fibnp2
    if len(str(fibn)) >= fiblen:
        break

print n
print fibn
print fibnp1
