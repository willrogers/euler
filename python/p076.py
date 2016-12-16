"""
How many ways can 100 be written as the sum of at least two positive integers?

This is almost precisely the partition function:
https://en.wikipedia.org/wiki/Partition_(number_theory)#Partition_function
"""
# Wikipedia tells us that p(100) is 190,569,292
p100 = 190569292
# Exclude 100 by itself.
print(p100 - 1)
