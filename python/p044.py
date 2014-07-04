'''
Find the two pentagonal numbers closest together whose
sum and difference are also pentagonal.

Pn = n(3n - 1)/2

The gaps between pentagonal numbers increases with n.
I generated all pentagonal numbers up to a certain number,
then checked that list, increasing the gaps between the 
numbers I was checking, and printing matches.
'''
import sys
import math

from utils import pentagons, is_pen


       
UPPER = 1000000000

pens = []
# build a list of pentagonal numbers
for p in pentagons():
    pens.append(p)
    if p > UPPER:
        break

STEPS = 10000
step = 1

if __name__ == "__main__":
    for step in range(1, STEPS):
        try: 
            for i, p in enumerate(pens):
                pdash = pens[i+step]
                pdiff = pdash-p
                psum = pdash + p
                psumpen = False
                pdiffpen = False
                if is_pen(psum):
                    psumpen = True
                if is_pen(pdiff):
                    pdiffpen = True
                if psumpen and pdiffpen:
                    print p, pdash, pdiff, psum
                    print "Matched!!"
                
        except IndexError:
            # done
            if step % 20 == 0:
                print "done step %s" % step


