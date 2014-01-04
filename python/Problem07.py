# Find the 10001st prime

from utils import is_prime
import sys


test = int(sys.argv[1])

print is_prime(test)

count = 0
no = 2

while True:
    if (is_prime(no)):
        count += 1
        print 'Prime ' + str(count) + ' = ' + str(no)
    no += 1
    
    if count == test:
        break

print 'Done'
