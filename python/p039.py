'''
For which value of p <= 1000 is the number of right-angled triangles with
integral lengths maximised?
'''
import math

# The maximum length of side is 500
squares = [ i*i for i in range(500) ]

tris = []

for i in range(1, 500):
    for j in range(1, 500):
        if (i*i + j*j) in squares:
            tris.append((i, j, int(round(math.sqrt(i*i + j*j)))))

# get unique values, if p <= 1000
tris = [ tuple(sorted(tri)) for tri in tris if sum(tri) <= 1000 ]
stris = set(tris)

tris2 = {i:0 for i in range(1001)}
for tri in stris:
    tris2[sum(tri)] += 1

maxp = 0
for key in tris2:
    if tris2[key] > maxp:
        maxp = tris2[key]
        print(key, tris2[key])

