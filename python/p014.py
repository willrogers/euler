'''
Find the longest chain starting below a million where:
if n is even, n = n / 2
if n is odd,  n = 3n + 1
and stopping at 1.

First attempt, after removing print statements and unnecessary function
calls, took about a minute.
'''

def collatz_num(n):
    l = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        l += 1
    return l


def run():
    max = (0,0)
    for i in range(1, 1000000):
        j = collatz_num(i)
        if j > max[1]:
            max = (i,j)
    print max[0]
    
run()
