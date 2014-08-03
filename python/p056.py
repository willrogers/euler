'''
For all numbers of the form a^b, a,b<100, what is the highest sum of the digits?
'''
maximum = 0

for i in range(100):
    for j in range(100):
        num = i**j
        digsum = sum(int(c) for c in str(num))
        if (digsum > maximum):
            maximum = digsum        

print(maximum)

# or...
maxsum = max([sum(int(c) for c in str(i**j)) for i in range(100) for j in range(100)])

print(maxsum)
