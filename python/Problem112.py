'''
https://projecteuler.net/problem=112
What's the lowest number for which the proportion of 'bouncy' numbers
is exactly 99%?
'''

def is_bouncy(n):
    not_forward = False
    not_back = False
    last = 0
    for i in str(n):
        if int(i) >= last:
            last = int(i)
        else:
            not_forward = True

    last = 0
    for i in reversed(str(n)):
        if int(i) >= last:
            last = int(i)
        else:
            not_back = True

    return not_forward and not_back

bouncy = 0
i = 1

while True:
    b = is_bouncy(i)
    if b:
        bouncy += 1

    f = float(bouncy)/ i
    if f == 0.99:
        print f, i, bouncy
        break

    i += 1

