"""
Darts.

Represent a shot by a tuple (value, multiple).
"""
import itertools

SINGLES = [(n+1, 1) for n in range(20)]
DOUBLES = [(n+1, 2) for n in range(20)]
TREBLES = [(n+1, 3) for n in range(20)]
INNER = (25, 2)
OUTER = (25, 1)
OUTSHOTS = DOUBLES + [INNER]
SHOTS = SINGLES + DOUBLES + TREBLES + [INNER] + [OUTER]


tot = 0
for o in OUTSHOTS:
    # These correspond to 1,2 and 3-shot finishes.
    for i in (0, 1, 2):
        # With replacement allows two shots the same
        for c in itertools.combinations_with_replacement(SHOTS, i):
            score = sum(s*m for s,m in list(c) + [o])
            if score < 100:
                tot +=1

print(tot)
