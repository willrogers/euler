import numpy
import utils
import collections
import logging as log
log.basicConfig()

FILENAME = 'p054_poker.txt'

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


class Hand(object):
    '''
    A hand as a numpy array is
    [[number, suit]
     ...
     [number, suit]]

    Member variables:
     - hand - the numpy array
     - rank - the type of hand
     - ordering - the list of integers used to distinguish between
                  hands of the same rank
    '''
    def __init__(self, hand):
        self.hand = hand
        self.rank = None
        self.ordering = []
        self._classify()

    def __str__(self):
        return 'Hand: {}, {}.'.format(self.rank, self.ordering)

    def __repr__(self):
        return self.__str__() + '\n{}'.format(self.hand)

    def __lt__(self, other):
        if self.rank == other.rank:
            log.debug('comparing ordering: {}, {}'.format(self.ordering, other.ordering))
            for o1, o2 in zip(self.ordering, other.ordering):
                log.debug(o1, o2)
                if o1 < o2:
                    log.debug('Returning True')
                    return True
                elif o1 > o2:
                    return False
        return self.rank < other.rank

    def __eq__(self, other):
        return self.rank == other.rank and self.ordering == other.ordering

    def flush(self):
        return len(set(self.hand[:,1])) == 1

    def straight_flush(self):
        return self.flush() and self.straight()

    def straight(self):
        numbers = self.hand[:,0]
        return max(numbers) - min(numbers) == 4 and len(set(numbers)) == 5

    def royal_flush(self):
        return self.straight_flush() and max(self.hand[:,0]) == 14

    def _classify_groups(self):
        groups = collections.Counter()
        order = []
        for i in range(5):
            groups[self.hand[i,0]] += 1
        for i in range(4,0,-1):
            for card in range(14,1,-1):
                try:
                    if groups[card] == i:
                        order.append(card)
                except KeyError:
                    pass
        self.ordering = order
        log.debug('Groups: {}'.format(groups))
        if len(groups) == 2:
            if set(groups.values()) == set([1,4]):
                self.rank = FOUR
            elif set(groups.values()) == set([2,3]):
                self.rank = FULL_HOUSE
        elif len(groups) == 3:
            if set(groups.values()) == set([2,2,1]):
                self.rank = TWO_PAIR
            elif set(groups.values()) == set([3,1,1]):
                self.rank = THREE
        elif len(groups) == 4:
            self.rank = PAIR
        else:
            self.rank = HIGH

    def _classify_flush(self):
        if self.royal_flush():
            self.rank = ROYAL_FLUSH
        elif self.straight_flush():
            self.rank = STRAIGHT_FLUSH
        else:
            self.rank = FLUSH
        self.ordering = list(reversed(sorted(self.hand[:,0])))

    def _classify(self):
        '''
        Set rank and ordering according to self.hand.
        '''
        if self.flush():
            self._classify_flush()
        elif self.straight():
            self.rank = STRAIGHT
            self.ordering = list(reversed(sorted(self.hand[:,0])))
        else:
            self._classify_groups()


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
    return Hand(hand)


def load_hands():
    file_string = utils.load_data(FILENAME)
    hands = []
    for line in file_string.split('\n'):
        parts = line.strip().split()
        hand1 = read_hand(parts[0:5])
        hand2 = read_hand(parts[5:10])
        hands.append((hand1, hand2))
    return hands

hands = load_hands()

test_hands = [[3,HEARTS,4,SPADES,6,SPADES,10,SPADES,12,CLUBS],
              [9,HEARTS,9,DIAMONDS,4,HEARTS,5,HEARTS,6,HEARTS],
              [9,HEARTS,9,DIAMONDS,6,SPADES,5,HEARTS,6,HEARTS],
              [9,HEARTS,9,DIAMONDS,9,SPADES,5,HEARTS,6,HEARTS],
              [2,SPADES,3,HEARTS,4,HEARTS,5,HEARTS,6,HEARTS],
              [8,HEARTS,3,HEARTS,4,HEARTS,5,HEARTS,6,HEARTS],
              [8,HEARTS,8,SPADES,4,HEARTS,4,CLUBS,8,DIAMONDS],
              [8,HEARTS,8,SPADES,4,HEARTS,8,CLUBS,8,DIAMONDS],
              [2,HEARTS,3,HEARTS,4,HEARTS,5,HEARTS,6,HEARTS],
              [14,HEARTS,13,HEARTS,10,HEARTS,11,HEARTS,12,HEARTS]]

def test():
    for i, th in enumerate(test_hands):
        hand = numpy.array(th).reshape(5,2)
        h = Hand(hand)
        log.debug('Hand {}: {} {}'.format(i, h.rank, h.ordering))

count = 0

for h1, h2 in hands:
    log.debug(h1, h2)
    assert(h1 != h2)
    if h1 > h2:
        count += 1

print(count)
