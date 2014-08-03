
def sumTo(n):
    total = 0
    for x in range(1, n):
        if ((x % 3 == 0) or (x % 5 == 0)):
            total += x
    return total


print((sumTo(1000)))
