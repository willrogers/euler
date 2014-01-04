'''
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

    print not_forward
    last = 10
    for i in reversed(str(n)):
        if int(i) <= last:
            last = int(i)
        else:
            not_back = True

    print not_back
    return not_forward and not_back

tests = [1, 2, 34, 1231, 12435, 212, 321]

for i in tests:
    b = is_bouncy(i)
    print i, b
