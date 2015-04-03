# http://projecteuler.net/problem=8
import utils

no_str = utils.load_data('p008_bignumber.txt')
no_str = ''.join(no_str.split())

CONSECUTIVE = 13
biggest = 0

for i, item in enumerate(no_str):
    try:
        prod = reduce(lambda x,y: x*y, (int(j) for j in no_str[i:i+13]))
    except IndexError: # index out of range - we've reached the end
        break
    if prod > biggest:
        biggest = prod

print(biggest)
