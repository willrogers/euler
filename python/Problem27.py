from utils import is_prime
UPPER = 1000

primes = []
for i in range(2, UPPER):
    if is_prime(i):
        primes.append(i)
        
print primes

# b must be prime and therefore positive
# a must be odd

def get_no_primes(a, b):
    ''' 
    Find the number of primes generated by an a, b pair.
    '''
    i = 0
    while True:
        if is_prime(i * i + a * i + b):
            i += 1
        else:
            if i == 71:
                print a, b, a * b
            return i


gen_ps = []
for b in primes:
    for a in range(-999, 999, 2):
        gen_ps.append(get_no_primes(a, b))

print max(gen_ps)
