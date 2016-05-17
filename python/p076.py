
# How many ways can 100 be written as the sum of at least two positive integers?


ITERATIONS = 6

start = ((1,1),)

def iterate(tups):
    next_tups = set()
    for tup in tups:
        for i, item in enumerate(tup):
            l = list(tup)
            l[i] = l[i] + 1
            next_tups.add(tuple(sorted(l)))
        l = list(tup)
        l.append(1)
        next_tups.add(tuple(sorted(l)))
    return next_tups


s = start
i = 2
while i <= 100:
    s = iterate(s)
    i += 1
    print(i, len(s))
