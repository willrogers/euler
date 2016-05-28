import unittest
import utils
import p062

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


class TestIntReplace(unittest.TestCase):

    def test_int_replace_for_one_replacement(self):
        ret = utils.int_replace(100, 3, [1], 2)
        self.assertEqual(ret, 120)

    def test_int_replace_with_leading_zero_replacements(self):
        ret = utils.int_replace(100, 3, [0,1], 2)
        self.assertEqual(ret, 20)

    def test_int_replace_with_no_replacements(self):
        ret = utils.int_replace(100, 3, [], 2)
        self.assertEqual(ret, 100)

    def test_int_replace_breaking_case(self):
        ret = utils.int_replace(100, 3, [1,2], 1)
        self.assertEqual(ret, 101)

    def test_int_replace_all_for_one_replacement(self):
        ret = utils.int_replace_all(100, 3, [1], 2)
        self.assertEqual(ret, 120)

    def test_int_replace_all_for_multiple_replacements(self):
        ret = utils.int_replace_all(100, 3, [0,1], 2)
        self.assertEqual(ret, 220)

    def test_int_replace_all_for_no_replacements(self):
        ret = utils.int_replace_all(100, 3, [], 2)
        self.assertEqual(ret, 100)


class TestPermutations(unittest.TestCase):

    def test_search_for_permutations(self):
        simple_perms = [12,21]
        perms = p062.search_for_permutations(simple_perms, 2)
        self.assertEqual(sorted(perms), simple_perms)

    def test_search_for_permutations_returns_empty_list_for_single_element(self):
        simple_perms = [12]
        perms = p062.search_for_permutations(simple_perms, 2)
        self.assertEqual(sorted(perms), [])

if __name__ == '__main__':
    unittest.main()
