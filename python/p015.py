'''
The number of paths to the bottom right are :

. . . 1
. 6 3 1 
. 3 2 1
1 1 1 1 

So each number is the sum of those to its right and below.
'''

# A 20x20 has 21x21 vertices
SIZE = 21

# Make sure not just to create SIZE copies of the same list.
l = [[0]*SIZE for i in range(SIZE)]

# Make two sides all ones
for i in range(SIZE):
    l[i][0] = 1

for j in range(SIZE):
    l[0][j] = 1

# Sum to find the rest of the numbers
for i in range(1, SIZE):
    for j in range(1, SIZE):
        l[i][j] = l[i-1][j] + l[i][j-1]


print(l[20][20])


