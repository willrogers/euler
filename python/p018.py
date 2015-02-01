"""
Find the max total value traversing the triangle from top to bottom.

At any stage, the next value from t[i][j] is either t[i+1][j] or t[i+1][j+1].
"""
import utils

DATAFILE = 'p018_triangle.txt'
TRIANGLE = utils.load_data(DATAFILE)

lines = TRIANGLE.strip().splitlines()
t = []
for line in lines:
    ints = [ int(i) for i in (line.split(" ")) ]
    t.append(ints)

HEIGHT = len(t)


def next_level(routes):
    longer_routes = []
    for route in routes:
        last = route[-1]
        new1 = route[:]
        new1.append(last)
        new2 = route[:]
        new2.append(last + 1)
        longer_routes.extend([new1, new2])
    return longer_routes

def get_routes(length):
    routes = [[0]]
    for i in range(length - 1):
        routes = next_level(routes) 
    return routes

routes = get_routes(HEIGHT)

# now try every route
vals = []
for route in routes:
    total = 0
    for i,j in zip(route, range(HEIGHT)):  
            total += t[j][i]
    vals.append(total)
print max(vals)
