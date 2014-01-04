# Find the sum of the digits in 100 factorial.

def fact(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    return total

print fact(100)

def sum_digits(n):
    total = 0
    # surely non-standard, but the first way I thought of doing it.
    for letter in str(n):
        total += int(letter)
    return total

print sum_digits(fact(100))
