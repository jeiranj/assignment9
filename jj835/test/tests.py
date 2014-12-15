import unittest
from checks import *

class checks_tests(unittest.TestCase):
    def test_year_bad(self):
        args = ['never','never1990','']
        for a in args:
            self.assertFalse(check_type(a))

    def test_year_good(self):
        self.assertTrue(check_type('1990'))

    def test_range_bad(self):
        first = '1990'
        last = '2000'
        args = ['200','20000']
        for a in args:
            self.assertFalse(check_range(a,first,last))

    def test_range_good(self):
        first = '1990'
        last = '2000'
        args = ['2000','1995','1990']
        for a in args:
            self.assertTrue(check_range(a,first,last))

suite = unittest.TestLoader().loadTestsFromTestCase(checks_tests)
unittest.TextTestRunner(verbosity=2).run(suite)            