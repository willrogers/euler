
values = [200, 100, 50, 20, 10, 5, 2, 1]
values = [5, 2, 1]
target = 5

answers = []
go = []

def next_try(last_try, coins, target):
    assert sum(last_try) >= target
    last = last_try.pop()
    try:
        next_coin = coins[coins.find(last) + 1]
    except IndexError:  
        return 

def attempt(coins, target):
    """ coins is ordered.  Return all valid attempts using the largest
        value in coins.
    """
    assert coins[0] <= target
    ans = []
    go = []
    for coin in coins:
        print "coin is", coin
        while sum(go) < target:
            go.append(coin)
            print "go is", go
        if sum(go) == target:
            return go
        else:
            go = go[:-1]
            continue

    return ans


answers = attempt(values, target)
print answers
