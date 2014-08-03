'''
Determine the shortest possible passcode for which the entries in 
keylog.txt could be valid login attempts.
'''
from collections import deque

FILE = 'data/keylog.txt'
attempts = []
with open(FILE) as f:
    for line in f:
        attempts.append(line.strip())

print(attempts)
#attempts = ['123', '234', '52']

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

i = 0 

def valid_pass(atts, pwd):
    for att in atts:
        if not valid_attempt(att, str(pwd)):
            return False

    return True

while True:
#    print i
    s = str(i)
    if '4' in s or '5' in s:
        continue

    if valid_pass(attempts, str(i)):
        break

    i += 1

print("done")
print(i)
    
print(valid_attempt('123', '1234'))
print(valid_attempt('234', '1234'))
    
