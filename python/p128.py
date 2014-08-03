
# http://projecteuler.net/problem=128
# Hexagons

from utils import is_prime
import time
import logging
logging.basicConfig(level=logging.DEBUG)


class Hexagon(object):
    
    count = 0
    hexagons = {}
    
    def __init__(self, num):
        self.num = num
        self.sides = {i:None for i in range(6)}

    def full(self):
        return not any(item == None for item in list(self.sides.values()))

    def __repr__(self):
        out = 'Hex %s: ' % self.num
        for i in range(6):
            side = self.sides[i]
            if side is None:
                out += 'n '
            else:
                out += str(self.sides[i].num) + ' ' 
        return out

    @staticmethod
    def get_next():
        Hexagon.count += 1
        h = Hexagon(Hexagon.count)
        Hexagon.hexagons[Hexagon.count] = h
        return h
    

def finish(innerh):
    """
    Fill surrounding hexagons in an anticlockwise direction.
    Start from the top, and only fill until you find one already there.
    """
    i = 0
    while innerh.sides[i] is None:
        i += 1
        continue
    while innerh.sides[i%6] is not None:
        if i == 6:
            break
        i += 1
        continue
    while innerh.sides[i % 6] is None:
        h = Hexagon.get_next()
        #logging.debug('creating side %s: %s' %  (i, h.num))
        # Attach new hex to inner hex
        innerh.sides[i % 6] = h
        h.sides[(i + 3) % 6] = innerh
        # Attach new hex to previous outer hex
        lasth = innerh.sides[(i-1)%6]
        if lasth is not None:
            h.sides[(i-2)%6] = lasth
            lasth.sides[(i+1)%6] = h
        # Attach new hex to next outer hex
        nexth = innerh.sides[(i+1)%6]
        if nexth is not None:
            h.sides[(i-4)%6] = nexth
            nexth.sides[(i-1)%6] = h
        if i == 6:
            break
        i += 1


def loop(starth, loopno):
    """
    Complete one loop of the hexagon shape.
    """
    if loopno == 2:
        n = 1
    else:
        n = (loopno - 2) * 6
    logging.info('looping ' +  str(starth))
    innerh = starth
    # put the first hexagon on the top
    nexth = Hexagon.get_next()
    nexth.sides[3] = starth
    starth.sides[0] = nexth
    logging.debug('created' + str(nexth))
    for i in range(n):
        logging.info('about to finish' +  str(innerh))
        finish(innerh)
        logging.info('finished' + str(innerh))
        innerh = Hexagon.hexagons[innerh.num + 1]

    # finish the loop
    lasth = Hexagon.hexagons[nexth.num + n]
    nexth.sides[4] = lasth
    lasth.sides[1] = nexth
    logging.debug('attached %s to %s' % (nexth.num, lasth.num))
    logging.debug('done loop\n\n')
    

def pd3(hexagon):
    tot = 0
    for side in list(hexagon.sides.values()):
        if is_prime(abs(side.num - hexagon.num)):
            tot += 1
    return tot == 3

        
def main():
    t = time.time()
    # create the first hexagon (loop 1)
    first = Hexagon.get_next()
    # create the second loop
    loop(first, 2)
    # create the rest of the loops
    for i in range(3, 100):
        print((i * i * 3) + i * 3 - 1, i)
        loop(Hexagon.hexagons[(i * i * 3) + i * 3 + 2], i)

    t = time.time() - t
    print(t)
    t = time.time()

    count = 0
    for hexagon in list(Hexagon.hexagons.values()):
        try:
            if pd3(hexagon):
                count += 1
                print(count, hexagon.num)
        except AttributeError:
            pass

    t = time.time() - t
    print(t)
    t = time.time()

if __name__ == '__main__':
    main()
