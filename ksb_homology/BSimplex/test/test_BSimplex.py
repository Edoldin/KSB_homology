import sys
ksb_homology_path="C:\\Users\\pjnav\\Desktop\\KSB_homology"
if ksb_homology_path not in sys.path:
    sys.path.append(ksb_homology_path)

import unittest
import numpy.matlib
import numpy as np
from ksb_homology.BSimplex import BSimplex as BS

#call python -m unittest BSimplex.test.test_BSimplex

class BSimplexTest(unittest.TestCase):

    def test_get_simplexsize_default(self):
        a=BS((1,2,4))
        self.assertEqual(a.get_simplexsize((1,2)), False)

    def test_get_partial_default(self):
        a=BS((1,2,4))
        self.assertEqual(a.get_partial((1,2),2), False)

    def test_get_mu_default(self):
        a=BS((1,2,4))
        self.assertEqual(a.get_mu((1,2),(2,3),2), False)

    def test_get_partial(self):
        a=BS((1,2,4))
        matrix=np.array([[1, 0],
                         [0, 1]])
        a.set_partial((1,2),2,matrix)
        solution=np.array_equal(a.get_partial((1,2),2), matrix)
        self.assertEqual(solution, True)
    
    def test_strictly_increasing(self):
        a=BS((1,2,4))
        a.set_partial((1,2),2,6)
        self.assertEqual(a.get_partial((1,2),2), 6)

    def test_is_Valid(self):
        a=BS((1,2,4))
        self.assertEqual(a.is_valid(), True)
        a=BS((1,2,4,3))
        self.assertEqual(a.is_valid(), False)
        a=BS(())
        self.assertEqual(a.is_valid(), False)

    def test_path(self):
        a=BS((1,2,3,4,5,6))
        print(a.path((1,2),(1,2,4,5,6)))
        self.assertEqual(a.path((1,2),(1,2,4,5,6)), ((1,2,4,5,6),(1,2,5,6),(1,2,6),(1,2)))
        self.assertEqual(a.path((1,2),(1,2,3,6)), ((1,2,3,6),(1,2,6),(1,2)))
        self.assertEqual(a.path((1,4),(1,3,4,6)), ((1,3,4,6),(1,4,6),(1,4)))

    '''def test_nCounter(self):
        a=BS((1,2,3,4))
        bot=(1,)
        top=(1,2,3)
        a.set_simplexsize((1,),1)
        a.set_simplexsize((1,2),3)
        a.set_simplexsize((1,2,3),2)
        solutionVal=[(1,1,1),(1,1,2),(1,2,1),(1,2,2),(1,3,1),(1,3,2)]
        #solutionVal=[(1,1,1),(1,1,2),(1,2,1),(1,2,2),(1,3,1),(1,3,2)]
        #los valores intermedios estarían acotados por los partial(sinplex, n)
        #el simplex sería
        solution=np.array_equal(a.nCounter(bot, top), solutionVal)
        self.assertEqual(solution, True)

        a.set_simplexsize((1,),2)
        solutionVal2=[(1,1,1),(1,1,2),(1,2,1),(1,2,2),(1,3,1),(1,3,2),
            (2,1,1),(2,1,2),(2,2,1),(2,2,2),(2,3,1),(2,3,2)]
        solution2=np.array_equal(a.nCounter(bot, top), solutionVal2)
        self.assertEqual(solution2, True)    '''

    def test_nCounter_2(self):
        print("test 123")
        a=BS((0,1))
        bot=set()
        top=((0,1))

        a.set_simplexsize(tuple(),2) #vacío
        a.set_simplexsize((0,),2)
        a.set_simplexsize((1,),2)
        a.set_simplexsize((0,1),2)
        #filas=filas
        partial1=np.array([[1, 3],
                           [1, 1]])
        a.set_partial((0,1),0,partial1)

        partial2=np.array([[1, 0],
                           [0, 1]])
        a.set_partial((0,1),1,partial2)

        partial3=np.array([[2, 1],
                           [2, 0]])
        a.set_partial((0,),0,partial3)

        partial4=np.array([[3, 7],
                           [2, 6]])
        a.set_partial((1,),1,partial4)

        print("nCounter",a.nCounter(bot,top))

        #buscar el valor de esto y mandarlo

        #solutionVal=[(1,1,1),(1,1,2),(1,2,1),(1,2,2),(1,3,1),(1,3,2)]
        #solutionVal=[(1,1,1),(1,1,2),(1,2,1),(1,2,2),(1,3,1),(1,3,2)]
        #los valores intermedios estarían acotados por los partial(sinplex, n)
        #el simplex sería
        #solution=np.array_equal(a.nCounter(bot, top), solutionVal)
        #self.assertEqual(solution, True)

        #a.set_simplexsize((1,),2)
        #solutionVal2=[(1,1,1),(1,1,2),(1,2,1),(1,2,2),(1,3,1),(1,3,2),
        #    (2,1,1),(2,1,2),(2,2,1),(2,2,2),(2,3,1),(2,3,2)]
        #solution2=np.array_equal(a.nCounter(bot, top), solutionVal2)
        #self.assertEqual(solution2, True)

    def test_build_S(self):
        a=BS((1,2,4))
        a.set_simplexsize((1,2),2)
        self.assertEqual( a.build_S(), ( ( (1,2),(1,2) ), ) )
        a.set_simplexsize((3,2),3)
        self.assertEqual( a.build_S(), ( ( (1,2),(1,2) ),( (3,2),(1,2,3) )) )
        #(simplex),(k=int, ... ) todo k<simplex_size(simplex)
        #((1,2,3),(1,3)) ejemplo de S
        #((1,2,3),(1,3)),((0,2,3),(4)) ejemplo de S
    
    #def test_2_proyective_planes_product(self):
    #    a=BS.proyective_planes_product_element()

    
    def test_sub_sequences(self):
        a=BS.sub_sequences((2,3,1))
        self.assertSetEqual(BS.sub_sequences((2,3,1)),{(1,3),(1,2),(2,3)})

if __name__ == '__main__':
    unittest.main()