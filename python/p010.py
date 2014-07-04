# Find the sum of all the primes below two million.
import math

def is_prime(n):
    if n == 1:
        return False
    max = int(math.sqrt(n)) + 1
    for i in range(2,max):
        if n % i == 0:
            return False
    return True

total = 0
for i in range(2000000):
    if is_prime(i):
        total += i
        print i

print total 


