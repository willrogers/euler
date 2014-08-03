# Find the 10001st prime

from utils import is_prime
import sys


TARGET = 10001


count = 0
no = 2

while True:
    if (is_prime(no)):
        count += 1
    no += 1
    
    if count == TARGET:
        print(no)
        break

