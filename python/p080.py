"""
Find the sum of the first 100 digits of the first 100 square roots if the roots
are not irrational.

I leaned on Python's exact decimal module for this.
"""
import decimal

# Avoid rounding errors by using a little extra precision.
decimal.getcontext().prec = 105
LIMIT = 100
total = 0

for i in range(1, LIMIT + 1):
    root = decimal.Decimal(i).sqrt()
    if root.to_integral_value() == root:  # exact root - ignore
        continue
    # remove decimal point
    bits = str(root).replace('.', '')
    # take the first 100 integers
    next = sum(int(j) for j in bits[:100])
    total += next

print(total)
