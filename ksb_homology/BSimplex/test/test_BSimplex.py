import unittest
from ksb_homology.BSimplex import BSimplex

#call python -m unittest BSimplex.test.test_BSimplex

class BSimplexTest(unittest.TestCase):

    def test_get_simplexsize_default(self):
        a=BSimplex((1,2,4))
        self.assertEqual(a.get_simplexsize((1,2)), False)

    def test_get_partial_default(self):
        a=BSimplex((1,2,4))
        self.assertEqual(a.get_partial((1,2),2), False)

    def test_get_mu_default(self):
        a=BSimplex((1,2,4))
        self.assertEqual(a.get_mu((1,2),(2,3),2), False)

    def test_get_partial(self):
        a=BSimplex((1,2,4))
        a.set_partial((1,2),2,6)
        self.assertEqual(a.get_partial((1,2),2), 6)

if __name__ == '__main__':
    unittest.main()