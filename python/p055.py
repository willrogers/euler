from utils import is_palindrome

# If not done in 50 tries, assume it won't create a palindrome.
ATTEMPTS = 50
LIMIT = 10000

def lychrel(n, attempts):
    """
    Return True if <n> is a Lychrel number given <attempts> iterations.
    """
    next_try = n
    for i in range(attempts):
        p = int(''.join(reversed(str(next_try))))
        next_try += p
        if is_palindrome(next_try):
            return False
    return True


# filter vs list comprehension
lychrels = filter(lambda x: lychrel(x, ATTEMPTS), range(LIMIT))
lychrels = [x for x in range(LIMIT) if lychrel(x, ATTEMPTS)]

print(len(lychrels))
