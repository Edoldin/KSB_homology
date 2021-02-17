import unittest
from BSimplex import BSimplex

#call python -m unittest BSimplex.test.test_BSimplex

class BSimplexTest(unittest.TestCase):

    def test_get_partial_defautl(self):
        a=BSimplex((1,2,4))
        self.assertEqual(a.get_partial((1,2),2), False)

    def test_get_partial(self):
        a=BSimplex((1,2,4))
        a.set_partial((1,2),2,6)
        self.assertEqual(a.get_partial((1,2),2), 6)

if __name__ == '__main__':
    unittest.main()