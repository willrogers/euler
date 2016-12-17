'''
Determine the shortest possible passcode for which the entries in 
keylog.txt could be valid login attempts.
'''
import itertools


FILE = 'data/keylog.txt'


def load_attempts(filename):
    attempts = []
    with open(FILE) as f:
        for line in f:
            attempts.append(line.strip())
    return attempts


def valid_attempt(att, pwd):
    done = 0
    next = att[done]
    for n in pwd:
        try:
            if n == next:
                done += 1
                next = att[done]
        except IndexError:
            return True
    return False


def valid_pass(atts, pwd):
    for att in atts:
        if not valid_attempt(att, str(pwd)):
            return False

    return True


if __name__ == '__main__':
    attempts = load_attempts(FILE)
    all_chars = set()
    for att in attempts:
        s = set(att)
        all_chars.update(s)
    # Try only the minimum-length permutations.
    for s in itertools.permutations(all_chars):
        if valid_pass(attempts, s):
            break

    print(''.join(i for i in s))

