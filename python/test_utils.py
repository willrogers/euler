import unittest
import utils

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_divisors(self):
        cases = {1:[], 2:[1], 3:[1], 4:[1,2], 6:[1,2,3], 28:[1,2,4,7,14]}
        for case in cases.keys():
            result = utils.divisors(case)
            if result != cases[case]:
                self.fail("Got the wrong divisors for %s: %s " % (case, str(cases[case])))

    def test_factors(self):
        cases = {1:[], 2:[2], 3:[3], 4:[2,2], 6:[2,3], 28:[2,2,7]}
        for case in cases.keys():
            result = utils.factors(case)
            if result != cases[case]:
                self.fail("Got the wrong factors for %s: %s " % (case, str(cases[case])))

    def test_is_prime(self):
        cases = {1: False, 2:True, 3:True, 4:False, 12:False, 23:True}
        for case in cases.keys():
            result = utils.is_prime(case)
            if result != cases[case]:
                self.fail("is_prime failed for %s: it got %s" % (case, result))

    def test_is_triangle(self):
        cases = {1:True, 2:False, 3:True, 6:True, 11:False, 55:True}
        for case in cases.keys():
            result = utils.is_triangle(case)
            if result != cases[case]:
                self.fail("is_triangle failed for %s: it got %s" % (case, cases[case]))

    def test_is_palinrome(self):
        cases = {1:True, 22:True, 23:False, "tenet":True, "hello":False}
        for case in cases.keys():
            result = utils.is_palindrome(case)
            if result != cases[case]:
                self.fail("is_palindrome failed for %s: it got %s" % (case, cases[case]))

    def test_is_square(self):
        cases = {1:True, 2:False, 3:False, 4:True}
        for case in cases:
            result = utils.is_square(case)
            if result != cases[case]:
                self.fail("is_square failed for %s: it got %s" % (case, result))

    def test_int_reverse(self):
        cases = {123:321, 1234:4321, 1:1, 134576:675431}
        for case in cases:
            result = utils.int_reverse2(case)
            if result != cases[case]:
                self.fail("is_square failed for %s: it got %s" % (case, result))

if __name__ == '__main__':
    unittest.main()
