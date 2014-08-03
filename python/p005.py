# What is the smallest positive number that is evenly divisible by all 
# of the numbers from 1 to 20?
import sys

# Get the number to test from the command-line argument.
MAX_NO = 20

def check_divis(n):
    for i in range(1, MAX_NO + 1):
        if n % i != 0:
            return False
    return True

latest = 1
while(True):
    # We only need to test multiples of the largest number.
    test = latest * MAX_NO
    if (check_divis(test)):
        break
    latest += 1

print(latest * MAX_NO)

