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
    
    def test_strictly_increasing(self):
        a=BSimplex((1,2,4))
        a.set_partial((1,2),2,6)
        self.assertEqual(a.get_partial((1,2),2), 6)

    def test_is_Valid(self):
        a=BSimplex((1,2,4))
        self.assertEqual(a.is_valid(), True)
        a=BSimplex((1,2,4,3))
        self.assertEqual(a.is_valid(), False)
        a=BSimplex(())
        self.assertEqual(a.is_valid(), False)
    
    def test_build_S(self):
        a=BSimplex((1,2,4))
        a.set_simplexsize((1,2),2)
        self.assertEqual( a.build_S(), ( ( (1,2),1 ),( (1,2),2 ) ) )
        a.set_simplexsize((3,3),3)
        self.assertEqual( a.build_S(), ( ( (1,2),1 ),( (1,2),2 ),( (3,3),1 ),( (3,3),2 ),( (3,3),3 ) ) )
    
    def test_sub_sequences(self):
        a=BSimplex.sub_sequences((2,3,1))
        self.assertSetEqual(BSimplex.sub_sequences((2,3,1)),{(1,3),(1,2),(2,3)})

if __name__ == '__main__':
    unittest.main()