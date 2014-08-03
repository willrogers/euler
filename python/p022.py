"""
For each item in the list of names, get an alphabetical score.  Then multiply
it by its position in the list to get an overall score.
"""

from utils import from_file

content  = from_file("../data/names.txt")

values = {}
for i in range(26):
    # ascii values of A - Z 
    values[chr(i + 65)] = i + 1

content = content.strip()
names = [ word.strip("\"") for word in content.split(",") ]

names = sorted(names)

total = 0

for i in range(len(names)):
    score = sum( [values[x] for x in names[i] ] )
    #score = reduce( lambda x, y: values[x] + values[y], names[i] ) 
    total += score * (i + 1)

print(total)
