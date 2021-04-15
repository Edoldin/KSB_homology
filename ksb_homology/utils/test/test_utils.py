import unittest
from ksb_homology.BSimplex import BSimplex as BS
from ksb_homology.utils import *

class BSimplexTest(unittest.TestCase):

    def test_calculate_index(self):
    
    def test_make_vector(self):
        self.assertEqual( make_vector( (1,2,3,4), 7 ), (True,True,True,True,False,False,False))
        self.assertEqual( make_vector( (3,5,6), 8 ), (False,False,True,False,True,True,False,False))

    def test_unmake(self):
        self.assertEqual( unmake_vector( (True,True,True,True,False,False,False), (1,2,3,4) ))
        self.assertEqual( unmake_vector( (False,False,True,False,True,True,False,False), (3,5,6) ))
    
    def test_smash(self):
    
    def test_add(self):
        T=defaultdict(lambda: False)
        add(T,((1,2),(3,4)))

    def test_kth_steenrod_square(self):
        X=BS.proyective_2planes_product_element()
        S=((),(1))
        sol=kth_steenrod_square( 2, X, S)
        self.assertEqual(kth_steenrod_square( 2, X, S), ((0,1),(1)) )



if __name__ == '__main__':
    unittest.main()