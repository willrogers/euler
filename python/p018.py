"""
Find the max total value traversing the triangle from top to bottom.

At any stage, the next value from t[i][j] is either t[i+1][j] or t[i+1][j+1].
"""

TRIANGLE = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

#TRIANGLE = '''
#3
#7 4
#2 4 6
#8 5 9 3
#'''

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

print "about to get routes"
routes = get_routes(HEIGHT)

# now try every route
vals = []
for route in routes:
    total = 0
    for i,j in zip(route, range(HEIGHT)):  
            total += t[j][i]
    vals.append(total)
print vals
print max(vals)
