"""
Square anagrams.
"""
import collections


FILE = 'data/p098_words.txt'


def load_words(filename):
    with open(filename) as f:
        content = f.read().strip()
        words = content.split(',')
        words = [word.strip('"') for word in words]
    return words


def find_anagrams(words):
    """
    Return a list of tuples containing anagrams from the word list,
    sorted by descending length.
    """
    anag_dict = collections.defaultdict(set)
    for word in words:
        letters = sorted(word)
        anag_dict[tuple(letters)].add(tuple(word))
    anags = [tuple(v) for v in anag_dict.values() if len(v) > 1]
    anags = sorted(anags, key=lambda x:len(x[0]), reverse=True)
    return anags

words = load_words(FILE)
print(words)
anags = find_anagrams(words)
for a in anags:
    print('{}: {}'.format(len(a[0]), a))
