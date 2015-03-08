"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each '_' is a single digit.

The integer must be a multiple of 10.
"""
import math
import re

# Assume the last two zeros
MIN = int(math.floor(math.sqrt(1.02e16)))
MAX = int(math.floor(math.sqrt(1.93e16)))

PATTERN = '1.2.3.4.5.6.7.8.9'

# Go backwards, on a hunch ...
for i in range(MAX, MIN, -1):
    n = i ** 2
    if re.match(PATTERN, str(n)):
        print i * 10
        break
