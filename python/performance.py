import timeit
import random

x = 24343 ** 100

def billion_string():
#    x = random.randint(1e10,1e1000)
    x = random.randint(1, 100) ** random.randint(1, 100)
    last_nine = str(x)[:9]
    return last_nine

def billion_int():
#    x = random.randint(1e10,1e1000)
    x = random.randint(1, 100) ** random.randint(1, 100)
    last_nine = x % 1000000000
    return last_nine

print("Strings vs ints")
print timeit.timeit(billion_string)
print timeit.timeit(billion_int)

def random_gen(n):
    for i in range(n):
        x = random.randint(1, 100) ** random.randint(1, 100)
        yield x

rands = [x for x in random_gen(1000)]

def div_diff():
    x = random.randint(1, 100) ** random.randint(1, 100)
    for i in rands:
        y = i % 1000

def div_same():
    x = random.randint(1, 100) ** random.randint(1, 100)
    for i in rands:
        y = x % 1000

print("Same vs diff")
print timeit.timeit(div_same, number=1000)
print timeit.timeit(div_diff, number=1000)
