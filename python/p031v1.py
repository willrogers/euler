'''
Find all the ways you can make up 2 pounds in British currency.
'''

LIMIT = 200

COINS = [1, 2, 5, 10, 20, 50, 100, 200]
REV_COINS = list(reversed(COINS))

attempts = []
attempt = {coin: 0 for coin in COINS}

def show(attempt):
    '''
    Display the dictionary of an attempt sensibly.
    '''
    for coin in REV_COINS:
        if attempt[coin] > 0:
            print coin, attempt[coin]

def next_attempt(last_attempt):
    '''
    Try to roll back the last try to the starting point of 
    the next try.  Then find the next possible combination
    from that starting point.

    The second part works, but going back the correct starting
    point is more difficult.
    '''
    
    print "Start:"
    show(last_attempt)
    start_from = 0
    for i, coin in enumerate(COINS):
        if last_attempt[coin] > 0:
            last_attempt[coin] -= 1
            start_from = len(COINS) - i
            break

    print "Rolled back to:"
    show(last_attempt)

    tot = sum(key * last_attempt[key] for key in last_attempt.keys())
        
    while tot < LIMIT:
        for coin in REV_COINS[start_from:]:
            while (LIMIT - tot) >= coin:
                last_attempt[coin] += 1
                tot += coin
                    
        
    return last_attempt
        
for i in range(10):
    na = next_attempt(attempt)
    print "Finish:"
    show(na)

