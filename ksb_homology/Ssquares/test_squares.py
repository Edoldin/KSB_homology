import sys, os
ksb_homology_path_list=os.path.dirname(os.path.realpath(__file__)).split("\\")[0:-2]
ksb_homology_path= "\\".join(ksb_homology_path_list)
if ksb_homology_path not in sys.path:
    sys.path.append(ksb_homology_path)

import unittest
from ksb_homology.Ssquares import Ssquares
from ksb_homology.BurnsideCube import BurnsideCube as BC

class SsquaresTest(unittest.TestCase):

    def setUpIncreaseValues(top,bot):
        uddot=sorted(set(top).difference(set(bot)))
        n=len(uddot)
        parallel=[[]]
        remain=[[]]
        circ=[uddot]
        for l in range(1,n):
            parallel.append(circ[0][0:l])
            circ.append(circ[0][l:n])
            remain.append([])
        return [parallel,circ,remain]

    def test_calculate_index(self):
        return 1

    '''def test_kth_steenrod_square(self):
        X=BS.proyective_2planes_product_element()
        S=((),(1))
        sol=kth_steenrod_square( 2, X, S)
        self.assertEqual(kth_steenrod_square( 2, X, S), ((0,1),(1)) )'''
    def test_increase1(self):
        parallel, circ, remain = SsquaresTest.setUpIncreaseValues([0,1,2,3],[])
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain)
        self.assertEqual(parallel,[[],[0],[0,1],[0,1,3]])
        self.assertEqual(circ,[[0,1,2,3],[1,2,3],[2,3],[2]])
        self.assertEqual(remain,[[],[],[],[]])
        self.assertEqual(pivot, 1)
        self.assertEqual(parpivot, 1)
        self.assertEqual(level, 3)
        self.assertEqual(stop, False)

    def test_increase2(self):
        parallel, circ, remain = SsquaresTest.setUpIncreaseValues([0,1,2,3],[])
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain)
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain)
        self.assertEqual(parallel,[[], [0], [0,1], [0,1]])
        self.assertEqual(circ,[[0,1,2,3], [1,2,3], [2,3], [2]])
        self.assertEqual(remain,[[],[],[],[3]])
        self.assertEqual(pivot, 1)
        self.assertEqual(parpivot, 2)
        self.assertEqual(level, 3)
        self.assertEqual(stop, False)
    
    def test_increase3(self):
        parallel, circ, remain = SsquaresTest.setUpIncreaseValues([0,1,2,3],[])
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain)
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain)
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain)
        self.assertEqual(parallel,[[], [0], [0,1], [0,1]])
        self.assertEqual(circ,[[0,1,2,3], [1,2,3], [2,3], [3]])
        self.assertEqual(remain,[[],[],[],[2]])
        self.assertEqual(pivot, 0)
        self.assertEqual(parpivot, 3)
        self.assertEqual(level, 3)
        self.assertEqual(stop, False)

    def test_increase4(self):
        parallel, circ, remain = SsquaresTest.setUpIncreaseValues([0,1,2,3],[])
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain)
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain)
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain)
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain)
        self.assertEqual(parallel,[[], [0], [0,2], [0,2,1]])
        self.assertEqual(circ,[[0,1,2,3], [1,2,3], [1,3], [3]])
        self.assertEqual(remain,[[],[],[],[]])
        self.assertEqual(pivot, 1) #algorithm sais 1
        self.assertEqual(parpivot, 1)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False)

    def test_increase5(self):
        parallel, circ, remain = SsquaresTest.setUpIncreaseValues([0,1,2,3],[])
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain)
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain)
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain)
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain)
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain)
        self.assertEqual(parallel,[[], [0], [0,2], [0,2,3]])
        self.assertEqual(circ,[[0,1,2,3], [1,2,3], [1,3], [1]])
        self.assertEqual(remain,[[],[],[],[]])
        self.assertEqual(pivot, 1)
        self.assertEqual(parpivot, 1)
        self.assertEqual(level, 3)
        self.assertEqual(stop, False)
    
    def test_complete_increase(self):
        parallel, circ, remain = SsquaresTest.setUpIncreaseValues([0,1,2],[])
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #1
        self.assertEqual(parallel,[[],[0],[0,2]])
        self.assertEqual(circ,[[0,1,2],[1,2],[1]])
        self.assertEqual(remain,[[],[],[]])
        self.assertEqual(pivot, 1)
        self.assertEqual(parpivot, 1)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False)

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #2
        self.assertEqual(parallel,[[],[0],[0]])
        self.assertEqual(circ,[[0,1,2],[1,2],[1]])
        self.assertEqual(remain,[[],[],[2]])
        self.assertEqual(pivot, 1)
        self.assertEqual(parpivot, 2)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False)

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #3
        self.assertEqual(parallel,[[],[0],[0]])
        self.assertEqual(circ,[[0,1,2],[1,2],[2]])
        self.assertEqual(remain,[[],[],[1]])
        self.assertEqual(pivot, 0)
        self.assertEqual(parpivot, 3)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False)

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #4
        self.assertEqual(parallel,[[],[1],[1,0]])
        self.assertEqual(circ,[[0,1,2],[0,2],[2]])
        self.assertEqual(remain,[[],[],[]])
        self.assertEqual(pivot, 1)
        self.assertEqual(parpivot, 1)
        self.assertEqual(level, 1)
        self.assertEqual(stop, False)

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #5
        self.assertEqual(parallel,[[],[1],[1,2]])
        self.assertEqual(circ,[[0,1,2],[0,2],[0]])
        self.assertEqual(remain,[[],[],[]])
        self.assertEqual(pivot, 1)
        self.assertEqual(parpivot, 1)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False)

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #6
        self.assertEqual(parallel,[[],[1],[1]])
        self.assertEqual(circ,[[0,1,2],[0,2],[0]])
        self.assertEqual(remain,[[],[],[2]])
        self.assertEqual(pivot, 1)
        self.assertEqual(parpivot, 2)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False)

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #7
        self.assertEqual(parallel,[[],[1],[1]])
        self.assertEqual(circ,[[0,1,2],[0,2],[2]])
        self.assertEqual(remain,[[],[],[0]])
        self.assertEqual(pivot, 0)
        self.assertEqual(parpivot, 3)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False)

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #8
        self.assertEqual(parallel,[[],[2],[2,0]])
        self.assertEqual(circ,[[0,1,2],[0,1],[1]])
        self.assertEqual(remain,[[],[],[]])
        self.assertEqual(pivot, 2)
        self.assertEqual(parpivot, 1)
        self.assertEqual(level, 1)
        self.assertEqual(stop, False)

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #9
        self.assertEqual(parallel,[[],[2],[2,1]])
        self.assertEqual(circ,[[0,1,2],[0,1],[0]])
        self.assertEqual(remain,[[],[],[]])
        self.assertEqual(pivot, 1)
        self.assertEqual(parpivot, 1)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False) 
 
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #10
        self.assertEqual(parallel,[[],[2],[2]])
        self.assertEqual(circ,[[0,1,2],[0,1],[0]])
        self.assertEqual(remain,[[],[],[1]])
        self.assertEqual(pivot, 1)
        self.assertEqual(parpivot, 2)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False) 
 
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #11
        self.assertEqual(parallel,[[],[2],[2]])
        self.assertEqual(circ,[[0,1,2],[0,1],[1]])
        self.assertEqual(remain,[[],[],[0]])
        self.assertEqual(pivot, 0)
        self.assertEqual(parpivot, 3)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False) 

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #12
        self.assertEqual(parallel,[[],[],[0]])
        self.assertEqual(circ,[[0,1,2],[0,1],[1]])
        self.assertEqual(remain,[[],[2],[2]])
        self.assertEqual(pivot, 2)
        self.assertEqual(parpivot, 2)
        self.assertEqual(level, 1)
        self.assertEqual(stop, False)
        
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #13
        self.assertEqual(parallel,[[],[],[1]])
        self.assertEqual(circ,[[0,1,2],[0,1],[0]])
        self.assertEqual(remain,[[],[2],[2]])
        self.assertEqual(pivot, 1)
        self.assertEqual(parpivot, 1)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False) 
 
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #14
        self.assertEqual(parallel,[[],[],[]])
        self.assertEqual(circ,[[0,1,2],[0,1],[0]])
        self.assertEqual(remain,[[],[2],[1, 2]])
        self.assertEqual(pivot, 1)
        self.assertEqual(parpivot, 2)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False) 
 
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #15
        self.assertEqual(parallel,[[],[],[]])
        self.assertEqual(circ,[[0,1,2],[0,1],[1]])
        self.assertEqual(remain,[[],[2],[0,2]])
        self.assertEqual(pivot, 0)
        self.assertEqual(parpivot, 3)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False) 

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #16
        self.assertEqual(parallel,[[],[],[0]])
        self.assertEqual(circ,[[0,1,2],[0,2],[2]])
        self.assertEqual(remain,[[],[1],[1]])
        self.assertEqual(pivot, 1)
        self.assertEqual(parpivot, 3)
        self.assertEqual(level, 1)
        self.assertEqual(stop, False) 

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #17
        self.assertEqual(parallel,[[],[],[2]])
        self.assertEqual(circ,[[0,1,2],[0,2],[0]])
        self.assertEqual(remain,[[],[1],[1]])
        self.assertEqual(pivot, 1)
        self.assertEqual(parpivot, 1)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False) 

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #18
        self.assertEqual(parallel,[[],[],[]])
        self.assertEqual(circ,[[0,1,2],[0,2],[0]])
        self.assertEqual(remain,[[],[1],[2,1]])
        self.assertEqual(pivot, 1)
        self.assertEqual(parpivot, 2)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False) 

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #19
        self.assertEqual(parallel,[[],[],[]])
        self.assertEqual(circ,[[0,1,2],[0,2],[2]])
        self.assertEqual(remain,[[],[1],[0,1]])
        self.assertEqual(pivot, 0)
        self.assertEqual(parpivot, 3)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False) 

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #20
        self.assertEqual(parallel,[[],[],[1]])
        self.assertEqual(circ,[[0,1,2],[1,2],[2]])
        self.assertEqual(remain,[[],[0],[0]])
        self.assertEqual(pivot, 0)
        self.assertEqual(parpivot, 3)
        self.assertEqual(level, 1)
        self.assertEqual(stop, False)

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #21
        self.assertEqual(parallel,[[],[],[2]])
        self.assertEqual(circ,[[0,1,2],[1,2],[1]])
        self.assertEqual(remain,[[],[0],[0]])
        self.assertEqual(pivot, 1)
        self.assertEqual(parpivot, 1)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False)

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #22
        self.assertEqual(parallel,[[],[],[]])
        self.assertEqual(circ,[[0,1,2],[1,2],[1]])
        self.assertEqual(remain,[[],[0],[2,0]])
        self.assertEqual(pivot, 1)
        self.assertEqual(parpivot, 2)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False)

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #23
        self.assertEqual(parallel,[[],[],[]])
        self.assertEqual(circ,[[0,1,2],[1,2],[2]])
        self.assertEqual(remain,[[],[0],[1,0]])
        self.assertEqual(pivot, 0)
        self.assertEqual(parpivot, 3)
        self.assertEqual(level, 2)
        self.assertEqual(stop, False)

        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain) #24
        self.assertEqual(stop, True)

    def test_local_mu(self):
        pp1=BC.Projective_plane()
        pp2=BC.Projective_plane()
        pp_Join=pp1.Join(pp2)

        vertex=(0,1)
        i,j=0,1
        one_double_sec=(((0,0,1,0,1)),((0,0,1,0,2)))
        level=0
        top=(0,1)
        Ssquares.local_mu(pp_Join,vertex,i,j,one_double_sec,level,top)
        self.assertEqual(one_double_sec, (((0,0,1,0,1)),((0,0,2,0,1))))

        one_double_sec=(((0,0,1,0,1)),((0,0,2,0,2)))
        Ssquares.local_mu(pp_Join,vertex,i,j,one_double_sec,level,top)
        self.assertEqual(one_double_sec, (((0,0,1,0,1)),((0,0,2,0,2))))

    def test_global_change(self):
        #Ssquares.global_change(X, nC, nC_adapted, level, pivot, parpivot)
        #Ssquares.global_change()
        return True
if __name__ == '__main__':
    unittest.main()