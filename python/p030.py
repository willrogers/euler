
POWER = 5
LIMIT = 1000000


for i in range(1,11):
    print("%d, %d\n", i, i ** POWER)

total = 0

for i in range(2, LIMIT):
    intstr = str(i)
    ints = [ int(j) for j in intstr ] 
    powsum = sum(k**POWER for k in ints)
    if powsum == i:
        print powsum
        total += powsum

print total
