"""
Find how many of the words in words.txt are triangle words.
All the words are upper case.
"""

from utils import from_file, is_triangle


values = {}
for i in range(26):
    # ascii values of A - Z 
    values[chr(i + 65)] = i + 1

print(values)

content = from_file("data/words.txt")
content = content.strip()

words = [ word.strip("\"") for word in content.split(",")]

tris = 0
for word in words:
    score = 0
    for letter in word:
        score += values[letter]
    if is_triangle(score):
        tris += 1

print("Number of words: ", len(words))
print("Number of triangle words: ", tris)



