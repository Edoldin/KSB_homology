import sys
ksb_homology_path="C:\\Users\\pjnav\\Desktop\\KSB_homology"
if ksb_homology_path not in sys.path:
    sys.path.append(ksb_homology_path)

import unittest
from ksb_homology.NCounter import NCounter as NC

class NCounterTest(unittest.TestCase):

    def test_getXkey(self):
        nc1=NC((1,2,2,4,1,3,2,4,3))
        self.assertEqual(nc1.getXkey(), [1,2,4,3,4])
        nc2=NC((1,2,3,4,5,6,7,8,9))
        self.assertEqual(nc2.getXkey(), [1,2,4,6,8])

    def test_getSkey(self):
        nc1=NC((1,2,2,4,1,3,2,4,3))
        self.assertEqual(nc1.getSkey(), [2,1,2,3])
        nc2=NC((1,2,3,4,5,6,7,8,9))
        self.assertEqual(nc2.getSkey(), [3,5,7,9])

    def test_mergeVertexAxis(self):
        nc=NC((1,2,3,4,5,6,7,8,9))
        self.assertEqual(NC.mergeVertexAxis(nc.getXkey(), nc.getSkey()), nc)

    def test_lexicographicNextValue(self):
        self.assertEqual(NC.lexicographicNextValue([1,1,3,4,5,6,7,8,9],(1,2,3,4,5,6,7,8,9)), [1,2,0,0,0,0,0,0,0])

    def test_arrayBiggerThan(self):
        self.assertEqual(NC.arrayBiggerThan((1,2,3,4,5,6,7,1,0), (1,2,3,4,5,6,7,1,0)),False)
        self.assertEqual(NC.arrayBiggerThan((1,2,3,4,5,6,7,1,0), (1,2,3,4,5,6,7,1,1)),False)
        self.assertEqual(NC.arrayBiggerThan((1,2,3,4,5,6,7,1,1), (1,2,3,4,5,6,7,1,0)),True)
        self.assertEqual(NC.arrayBiggerThan((1,2,3,5,5,6,7,1,0), (1,2,3,4,5,6,7,1,0)),True)

if __name__=='__main__':
    unittest.main()