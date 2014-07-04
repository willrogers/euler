"""
Find the sum of the numbers on the diagonals of a 1001 * 1001 spiral.
"""

SIZE = 1001
NUMBERS = SIZE * SIZE

assert SIZE % 2 == 1

centre = SIZE/2 
x = centre
y = centre
grid = [[None] * SIZE for i in range(SIZE)]

length = 1
flength = True
point = 0
direction = 'e'
for i in range(1, NUMBERS + 1):
    grid[x][y] = i
    point += 1
    if direction == 'e':
        x += 1
    elif direction == 's':
        y += 1
    elif direction == 'w':
        x -= 1
    elif direction == 'n':
        y -= 1
    else:
        raise Exception()
    if point == length:
        if direction == 'e':
            direction = 's'
        elif direction == 's':
            direction = 'w'
        elif direction == 'w':
            direction = 'n'
        elif direction == 'n':
            direction = 'e'
        else:
            raise Exception()
        point = 0
        if not flength:
            length += 1
        flength = not flength

diag = 0
for i in range(SIZE):
    diag += grid[i][i]
    diag += grid[i][SIZE-i-1]


diag -= 1

print diag
    

