
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
# Anyway, ignore the above; you don't have to be smart, this is python.

from cStringIO import StringIO

# Need a StringIO because concatenating strings
# in pypy is extremely slow.
s = StringIO()
i = 1
length = 0
while length < 10000000:
    s.write(str(i))
    length += len(str(i))
    i += 1

s = s.getvalue()

tot = 1
for i in range(7):
    tot *= int(s[1*10**i - 1])

print tot


