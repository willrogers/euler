'''
How many n-digit positive integers exist which are also an nth power?

10^x has x+1 digits, so we only need to consider single-digit numbers.
At some point, 9*x will have fewer than x digits, which is where we stop.
'''
import itertools

RESULTS = []

# n^0 is 1, so we can skip power 0.
for power in itertools.count(1):
    # If we haven't found an answer for some power, there
    # can't be any answers for bigger powers.
    found = False
    for i in itertools.count(1):
        n = i**power
        l = len(str(n))
        if l == power:
            found = True
            RESULTS.append((i,power,n))
        # Too big; move on to the next power.
        elif l > power:
            break
    # No answer for this power; no more answers.
    if not found:
        break

print len(RESULTS)
        
