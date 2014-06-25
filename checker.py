import sys

SOLUTIONS = 'solutions.txt'

answers = {}

with open(SOLUTIONS) as f:
    for line in f.readlines():
        # remove dot
        parts = line.split()
        try:
            num = int(parts[0][:-1])
            answers[num] = parts[1]
        except:
            pass

try:
    key = int(sys.argv[1])
    answer = str(sys.argv[2])
except IndexError:
    print 'Usage: %s <no> <answer>' % sys.argv[0]
    sys.exit()

if answers[key] == answer:
    print "correct"
else:
    print "incorrect"

