import sys, os
ksb_homology_path_list=os.path.dirname(os.path.realpath(__file__)).split("\\")[0:-2]
ksb_homology_path= "\\".join(ksb_homology_path_list)
if ksb_homology_path not in sys.path:
    sys.path.append(ksb_homology_path)

import unittest
from ksb_homology.Utils import Utils as ut

class BurnsideCubeTest(unittest.TestCase):

    def test_calculate_index(self):
        return 1

    def test_make_vector(self):
        self.assertEqual( ut.make_vector( (1,2,3,4), 7 ), [True,True,True,True,False,False,False])
        self.assertEqual( ut.make_vector( (3,5,6), 8 ), [False,False,True,False,True,True,False,False])

    def test_unmake(self):
        self.assertEqual( ut.unmake_vector( (True,True,True,True,False,False,False)), [1,2,3,4] )
        self.assertEqual( ut.unmake_vector( (False,False,True,False,True,True,False,False)), [3,5,6] )

    def test_ordered_union(self):
        priorityList=(3,4,5)
        extension=(1,2,3)
        self.assertEqual(ut.ordered_union(priorityList,extension, False), [3,4,5,1,2])
        self.assertEqual(ut.ordered_union(priorityList,extension, True),  [1,2,3,4,5])
        priorityList=(4,3,5)
        extension=(1,3,2)
        self.assertEqual(ut.ordered_union(priorityList,extension, False), [4,3,5,1,2])
        self.assertEqual(ut.ordered_union(priorityList,extension, True),  [1,2,4,3,5])

    def test_ordered_difference(self):
        priorityList=[1,2,4,3,5]
        difference=[1,2,3]
        self.assertEqual(ut.ordered_difference(priorityList,difference), [4,5])
        priorityList=[4,3,5,1,2]
        self.assertEqual(ut.ordered_difference(priorityList,difference), [4,5])
        difference=[3]
        self.assertEqual(ut.ordered_difference(priorityList,difference), [4,5,1,2])
        difference=[5,1,2]
        self.assertEqual(ut.ordered_difference(priorityList,difference),  [4,3])

    def test_matrix_direct_sum_2d(self):
        m1=[[1,1,1],
            [1,1,1],
            [1,1,1]]

        m2=[[2,2,2,2],
            [2,2,2,2]]

        m1_m2=[ [1,1,1,0,0,0,0],
                [1,1,1,0,0,0,0],
                [1,1,1,0,0,0,0],
                [0,0,0,2,2,2,2],
                [0,0,0,2,2,2,2],]

        sol=ut.matrix_direct_sum_2d(m1, m2)
        self.assertEqual(sol, m1_m2)

    def test_square_repmat_in(self):
        '''
        k * [ [a,b],
              [c,d] ]
            ||
        [[ a, b,  (a, b)],
         [ c, d,  (c, d)],
         [(a, b), (a, b)],
         [(c, d), (c, d)] ]
        '''
        m=[ [1,2],
            [3,4] ]
        mrep2=[[1, 2, 1, 2],
               [3, 4, 3, 4],
               [1, 2, 1, 2],
               [3, 4, 3, 4] ]
        mrep4=[[1, 2, 1, 2, 1, 2, 1, 2],
               [3, 4, 3, 4, 3, 4, 3, 4],
               [1, 2, 1, 2, 1, 2, 1, 2],
               [3, 4, 3, 4, 3, 4, 3, 4],
               [1, 2, 1, 2, 1, 2, 1, 2],
               [3, 4, 3, 4, 3, 4, 3, 4],
               [1, 2, 1, 2, 1, 2, 1, 2],
               [3, 4, 3, 4, 3, 4, 3, 4] ]

        self.assertEqual(ut.square_repmat_in(2,m), mrep2)
        self.assertEqual(ut.square_repmat_in(4,m), mrep4)
        m2=[[1],
            [3] ]
        m2rep2=[[1, 1],
                [3, 3],
                [1, 1],
                [3, 3] ]
        self.assertEqual(ut.square_repmat_in(2,m2), m2rep2)

    def test_square_repmat_out(self):
        '''
        [ [a,b],  * k
            [c,d] ]
            ||
        [ [ a, (a),  b,  (b)],
            [(a),(a), (b), (b)],
            [ c, (c),  d,  (d)],
            [(c),(c), (d), (d)] ]
        '''
        m=[ [1,2],
            [3,4] ]

        mrep2=[[1, 1, 2, 2],
               [1, 1, 2, 2],
               [3, 3, 4, 4],
               [3, 3, 4, 4] ]

        mrep4=[[1, 1, 1, 1, 2, 2, 2, 2],
               [1, 1, 1, 1, 2, 2, 2, 2],
               [1, 1, 1, 1, 2, 2, 2, 2],
               [1, 1, 1, 1, 2, 2, 2, 2],
               [3, 3, 3, 3, 4, 4, 4, 4],
               [3, 3, 3, 3, 4, 4, 4, 4],
               [3, 3, 3, 3, 4, 4, 4, 4],
               [3, 3, 3, 3, 4, 4, 4, 4] ]
               
        self.assertEqual(ut.square_repmat_out(m,2), mrep2)
        self.assertEqual(ut.square_repmat_out(m,4), mrep4)

        m2=[[1],
            [3] ]
        m2rep2=[[1, 1],
                [1, 1],
                [3, 3],
                [3, 3] ]
        self.assertEqual(ut.square_repmat_out(m2,2), m2rep2)

if __name__ == '__main__':
    unittest.main()