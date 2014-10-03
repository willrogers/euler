import timeit
import random

def billion_string():
    x = random.randint(1e10,1e20)
    last_nine = str(x)[:9]
    return last_nine

def billion_int():
    x = random.randint(1e10,1e20)
    last_nine = x % 1e9
    return last_nine

print("Strings vs ints")
print timeit.timeit(billion_string)
print timeit.timeit(billion_int)
