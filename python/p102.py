"""
A point is inside a triangle if:

* for each of three sets of points
* given a straight line containing two of the points
* it is on the same side of that line as the third point
"""
import utils
import itertools

FILENAME = 'p102_triangles.txt'

class Line(object):
    def __init__(self, pt1, pt2):
        try:
            self.a = 1.0 * (pt1[1] - pt2[1]) / (pt1[0] - pt2[0])
            self.b = pt1[1] - self.a * pt1[0]
            self.vertical = False
        except ZeroDivisionError:
            self.x = pt1[0]
            self.vertical = True

    def below(self, point):
        # Return True or False
        assert not self.vertical
        return point[1] > self.a * point[0] + self.b

    def left_of(self, point):
        # Return True or False
        assert self.vertical
        return point[0] > self.x


def point_in_triangle(point, vertices):
    pairs = itertools.combinations((0,1,2), 2)
    for p1, p2 in pairs:
        l = Line(vertices[p1], vertices[p2])
        p3 = vertices[3-p1-p2]
        if l.vertical:
            if l.left_of(p3) != l.left_of(point):
                return False
        else:
            if l.below(p3) != l.below(point):
                return False

    return True

if __name__ == '__main__':
    data = utils.load_data(FILENAME)
    tot = 0
    for line in data.split('\n'):
        nums = line.strip().split(',')
        nums = [int(num) for num in nums]
        p1 = nums[0], nums[1]
        p2 = nums[2], nums[3]
        p3 = nums[4], nums[5]
        if point_in_triangle((0, 0), (p1, p2, p3)):
            tot += 1

    print tot
