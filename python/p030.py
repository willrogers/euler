
POWER = 5
LIMIT = 1000000


total = 0

for i in range(2, LIMIT):
    intstr = str(i)
    ints = [ int(j) for j in intstr ] 
    powsum = sum(k**POWER for k in ints)
    if powsum == i:
        total += powsum

print(total)
