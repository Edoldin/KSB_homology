import sys, os
ksb_homology_path_list=os.path.dirname(os.path.realpath(__file__)).split("\\")[0:-2]
ksb_homology_path= "\\".join(ksb_homology_path_list)
if ksb_homology_path not in sys.path:
    sys.path.append(ksb_homology_path)

import unittest
import numpy.matlib
import numpy as np
from ksb_homology.BurnsideCube import BurnsideCube as BC

#call python -m unittest BurnsideCube.test.test_BurnsideCube
''''
implementar los 3 ejemplos del pdf
'''
class BurnsideCubeTest(unittest.TestCase):

    def test_get_size_default(self):
        a=BC(4)
        self.assertEqual(a.get_size((1,2)), 0)
        self.assertRaises(TypeError, a.get_size,[1,2])

    def test_get_partial_default(self):
        BurnsideCube=BC(4)
        self.assertEqual(BurnsideCube.get_partial((1,2),2), 0)
        BurnsideCube.set_size((1,2),1)
        self.assertEqual(BurnsideCube.get_partial((1,2),2), 0)
        BurnsideCube.set_size((1,),1)
        self.assertRaises(Exception, BurnsideCube.get_partial, (1,2))

    def test_get_mu_default(self):
        a=BC(4)
        self.assertEqual(a.get_mu((1,2),(2,3),2), False)

    #def test_get_partial(self):
    #    a=BC(4)
    #    a.set_size((1,2),1)
    #    a.set_size((1),1)
    #    matrix=np.array([[1, 0],
    #                     [0, 1]])
    #    a.set_partial((1,2),2,matrix)
#
    #    solution=np.array_equal(a.get_partial((1,2),2), matrix)
    #    self.assertEqual(solution, True)
    
    #def test_strictly_increasing(self):
    #    a=BC(4)
    #    a.set_partial((1,2),2,[[6]])
    #    self.assertEqual(a.get_partial((1,2),2), [[6]])

    def test_is_Valid(self):
        a=BC(4)
        self.assertEqual(a.is_valid(), True)
        a=BC(0)
        self.assertEqual(a.is_valid(), False)

    def test_path(self):
        a=BC(6)
        #print(a.path((1,2),(1,2,4,5,6)))
        self.assertEqual(a.path((1,2),(1,2,4,5,6)), ((1,2,4,5,6),(1,2,5,6),(1,2,6),(1,2)))
        self.assertEqual(a.path((1,2),(1,2,3,6)), ((1,2,3,6),(1,2,6),(1,2)))
        self.assertEqual(a.path((1,4),(1,3,4,6)), ((1,3,4,6),(1,4,6),(1,4)))

    def test_double_seq(self):
        a=BC(3)
        bot=set()
        top=((1,2))

        a.set_size(tuple(),2)
        a.set_size((1,),2)
        a.set_size((2,),2)
        a.set_size((1,2),2)

        partial1=np.array([[1, 3],
                           [1, 1]])
        a.set_partial((1,2),0,partial1)

        partial2=np.array([[1, 0],
                           [0, 1]])
        a.set_partial((1,2),1,partial2)

        partial3=np.array([[2, 1],
                           [2, 0]])
        a.set_partial((1,),0,partial3)

        partial4=np.array([[3, 7],
                           [2, 6]])
        a.set_partial((2,),1,partial4)

        double_sec_Solution=[(0, 0, 1, 0, 1), (0, 0, 1, 0, 2), (0, 0, 1, 0, 3), (0, 0, 1, 1, 1), (0, 0, 1, 1, 2), (0, 1, 1, 0, 1), (0, 1, 1, 0, 2), (0, 1, 1, 0, 3), (0, 1, 1, 0, 4), (0, 1, 1, 0, 5), (0, 1, 1, 0, 6), (0, 1, 1, 0, 7), (0, 1, 1, 1, 1), (0, 1, 1, 1, 2), (0, 1, 1, 1, 3), (0, 1, 1, 1, 4), (0, 1, 1, 1, 5), (0, 1, 1, 1, 6), (1, 0, 1, 0, 1), (1, 0, 1, 0, 2), (1, 0, 1, 0, 3), (1, 0, 2, 0, 0), (1, 0, 2, 0, 1), (1, 0, 2, 0, 2), (1, 0, 2, 0, 3), (1, 0, 3, 0, 0), (1, 0, 3, 0, 1), (1, 0, 3, 0, 2), (1, 0, 3, 0, 3), (1, 0, 1, 1, 1), (1, 0, 1, 1, 2), (1, 0, 2, 1, 0), (1, 0, 2, 1, 1), (1, 0, 2, 1, 2), (1, 0, 3, 1, 0), (1, 0, 3, 1, 1), (1, 0, 3, 1, 2), (1, 1, 1, 0, 1), (1, 1, 1, 0, 2), (1, 1, 1, 0, 3), (1, 1, 1, 0, 4), (1, 1, 1, 0, 5), (1, 1, 1, 0, 6), (1, 1, 1, 0, 7), (1, 1, 1, 1, 1), (1, 1, 1, 1, 2), (1, 1, 1, 1, 3), (1, 1, 1, 1, 4), (1, 1, 1, 1, 5), (1, 1, 1, 1, 6)]
        path=a.path(bot,top,False) #el primer elemento es el más alto
        double_seq=a.double_seq(path)
        print(path)
        for k in double_seq:
            print(k)
        self.assertEqual( double_seq, double_sec_Solution )

    def test_build_S(self):
        a=BC(4)
        a.set_size((1,2),2)
        self.assertEqual( a.build_S(), ( ( (1,2),(1,2) ), ) )
        a.set_size((3,2),3)
        self.assertEqual( a.build_S(), ( ( (1,2),(1,2) ),( (3,2),(1,2,3) )) )
        #(simplex),(k=int, ... ) todo k<simplex_size(simplex)
        #((1,2,3),(1,3)) ejemplo de S
        #((1,2,3),(1,3)),((0,2,3),(4)) ejemplo de S
    
    #def test_2_proyective_planes_product(self):
    #    a=BC.proyective_planes_product_element()
    def test_len(self):
        a=BC.Projective_plane()
        self.assertEqual(len(a),1)

    
    def test_sub_sequences(self):
        self.assertSetEqual(BC.sub_sequences((2,3,1)),{(2,3),(1,3),(1,2)})

    def test_Dual(self):
        pp=BC.Projective_plane()
        pp_dual=pp.Dual()
        self.assertEqual(pp.is_equal(pp_dual),True)

    def test_Join(self):
        pp1=BC.Projective_plane()
        pp2=BC.Projective_plane()

        pp_Join=pp1.Join(pp2)
        join_cube=BC(2)
        join_cube.set_size([],1)
        join_cube.set_size([0],1)
        join_cube.set_size([1],1)
        join_cube.set_size([0,1],1,2)
        join_cube.set_partial([0],0,2)
        join_cube.set_partial([1],1,2)
        join_cube.set_partial([0,1],0,2)
        join_cube.set_partial([0,1],1,2)

        self.assertEqual(join_cube.is_equal(pp_Join),True)
    
    def test_trebol(self):
        simplex=BC(3)
        simplex.set_size((),1)
        simplex.set_size((0,),1)
        simplex.set_partial((0,),1,[[2]])
        return simplex

if __name__ == '__main__':
    unittest.main()