# Find the sum of the digits in 2^100.
# Version 2: some tidying.

def sum_digits(n):
    total = 0
    # surely non-standard, but the first way I thought of doing it.
    for letter in str(n):
        total += int(letter)
    return total

print sum_digits(2 ** 1000)

