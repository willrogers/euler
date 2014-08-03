"""
What's the first triangle number to have over 500 divisors?
"""

from utils import triangle, divisors2, factors

threshold = 500

i = 1

most = 0

while True:
    t = triangle(i)
    d = divisors2(t)
    d.append(i) # divisors doesn't include number itself.
    if len(d) > most:
        most = len(d)
    if len(d) > threshold:
        print(t)
        break
    else:
        i = i + 1

