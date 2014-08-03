
l = list()

l.append(1)
l.append(2)


for i in range(2, 4000):
    l.append(l[i-1] + l[i-2])
    if (l[i] >= 4000000):
        break

total = 0
for item in l:
    if (item % 2 == 0):
        total += item

print total


