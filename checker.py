#!/usr/bin/env python
import sys

SOLUTIONS = 'solutions.txt'

def load_solutions(filename):
    answers = {}
    with open(filename) as f:
        for line in f.readlines():
            # remove dot
            parts = line.split()
            try:
                num = int(parts[0][:-1])
                answers[num] = parts[1]
            except:
                pass
    return answers


if __name__ == '__main__':
    answers = load_solutions(SOLUTIONS)
    try:
        key = int(sys.argv[1])
        answer = str(sys.argv[2])
    except IndexError:
        print 'Usage: %s <no> <answer>' % sys.argv[0]
        sys.exit(2)

    if answers[key] == answer:
        sys.exit(0)
    else:
        sys.exit(1)

