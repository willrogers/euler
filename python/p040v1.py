
# 9 numbers have 1 digit
# 90 numbers have 2 digits
# 900 numbers have 3 digits
# ...
# So the length of the concatenation is 
#  = 9 * 1 + 90 * 2 + 900 * 3 ...
#  = 9 * (n * 10**(n-1))

# The first digit falls in 9
# The tenth digit falls in 90 * 2
# The hundredth digit falls in 90 * 2
# ...
# You don't have to be smart, this is python.

s = ""
i = 1
while len(s) < 10000000:
    s += str(i)
    i += 1

tot = 1
for i in range(7):
    tot *= int(s[1*10**i - 1])

print tot 


