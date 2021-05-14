import sys, os
ksb_homology_path_list=os.path.dirname(os.path.realpath(__file__)).split("\\")[0:-2]
ksb_homology_path= "\\".join(ksb_homology_path_list)
if ksb_homology_path not in sys.path:
    sys.path.append(ksb_homology_path)

import unittest
from ksb_homology.Utils import Utils

class SsquaresTest(unittest.TestCase):

    def test_calculate_index(self):
        return 1

    '''def test_kth_steenrod_square(self):
        X=BS.proyective_2planes_product_element()
        S=((),(1))
        sol=kth_steenrod_square( 2, X, S)
        self.assertEqual(kth_steenrod_square( 2, X, S), ((0,1),(1)) )'''



if __name__ == '__main__':
    unittest.main()