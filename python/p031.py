
COINS = [200, 100, 50, 20, 10, 5, 2, 1]
TARGET = 200


def next_try(target, go):
    # remove 1s from the end
    while go[-1] == COINS[-1]:
        go.pop()
    # what was the last coin which wasn't 1?
    last = go.pop()
    next_smallest = COINS[COINS.index(last) + 1]
    while sum(go) < target:
        go.append(next_smallest)

    return go


n = [COINS[0]]
answers = [n]
while set(n) != set([COINS[-1]]):
    n = next_try(TARGET, n)
    if sum(n) == TARGET:
        answers.append(n)

print(len(answers))
