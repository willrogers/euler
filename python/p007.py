# Find the 10001st prime

from utils import is_prime
import sys


TARGET = 10001

# Start at 1 so we can test only odd numbers
count = 1
no = 1

while count < TARGET:
    no += 2
    if (is_prime(no)):
        count += 1

print no


