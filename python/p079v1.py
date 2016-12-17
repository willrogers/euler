'''
Determine the shortest possible passcode for which the entries in 
keylog.txt could be valid login attempts.
'''
from collections import deque


FILE = 'data/keylog.txt'


def load_attempts(filename):
    attempts = []
    with open(FILE) as f:
        for line in f:
            attempts.append(line.strip())
    return attempts


def valid_attempt(att, pwd):
    da = deque(att)
    c = da.popleft()
    try:
        for ch in pwd:
            if ch == c:
                c = da.popleft()
    except IndexError:
        return True

    return False


def valid_attempt2(att, pwd):
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
        if not valid_attempt2(att, str(pwd)):
            return False

    return True


if __name__ == '__main__':
    attempts = load_attempts(FILE)
    all_chars = set()
    for att in attempts:
        s = set(att)
        all_chars.update(s)
    missing_chars = (set(str(i) for i in range(10))).difference(all_chars)
    i = 0
    while True:
        i += 1
        s = str(i)
        if not set(s) == all_chars:
            continue
        if valid_pass(attempts, s):
            break

    print(i)

