import numpy

HIGH = 0
PAIR = 1
TWO_PAIR = 2
THREE = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR = 7
STRAIGHT_FLUSH = 8
ROYAL_FLUSH = 9

HEARTS = 0
SPADES = 1
CLUBS = 2
DIAMONDS = 3

SUITS = {'H': HEARTS,
         'S': SPADES,
         'C': CLUBS,
         'D': DIAMONDS}

ROYALS = {'T': 10,
          'J': 11,
          'Q': 12,
          'K': 13,
          'A': 14}


def classify_flush(hand):
    print('Classfying %s' % hand)
    if max(hand[:,0]) - min(hand[:,0]) == 4:
        if max(hand[:,0]) == 14:
            return ROYAL_FLUSH
        else:
            return STRAIGHT_FLUSH
    else:
        return FLUSH

def classify_groups(hand):
    cards = defaultdict(list)
    for card in hand:
        print('Card is %s' % card)
        cards[card[1]].append(card[0])
    print('Classifying groups for hand %s' % hand)
    print(cards)
    best = None
    second = None
    for suit in cards.itervalues():
        if len(suit) == 4:
            best = FOUR, max(suit)
        elif len(suit) == 3:
            max_suit = len(suit)
            max_num = max(suit)
        elif len(suit) > sec_suit

def classify(hand):
    if len(set(hand[:,1])) == 1:
        return classify_flush(hand)
    else:
        return classify_groups(hand)

def read_hand(strings):
    hand = numpy.zeros([5,2])
    for i, item in enumerate(strings):
        try:
            num = int(item[0])
        except ValueError:
            num = ROYALS[item[0]]
        suit = SUITS[item[1]]
        hand[i, 0] = num
        hand[i, 1] = suit
    # sort by card number
    return numpy.sort(hand, axis=0)


def load(filename):
    hands = []
    with open(filename) as f:
        for line in f:
            parts = line.split()
            hand1 = read_hand(parts[0:5])
            hand2 = read_hand(parts[5:10])
            hands.append((hand1, hand2))
    return hands

hands = load('../data/p054_poker.txt')

print(hands[0])
print(len(hands))

hand = [2,HEARTS,3,HEARTS,4,HEARTS,5,HEARTS,6,HEARTS]
hand = numpy.array(hand).reshape(5,2)
print hand
print(classify(hand))
print(classify(hands[0][0]))
