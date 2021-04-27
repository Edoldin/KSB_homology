import unittest
from ksb_homology.NCounter import NCounter as NC

class BSimplexTest(unittest.TestCase):

    def test_getXkey(self,vertexValues,edges):
        nc1=NC((1,2,2,4,1,3,2,4,3))
        self.assertEqual(nc1.getSkey(), (1,2,4,3,4))
        nc2=NC((1,2,3,4,5,6,7,8,9))
        self.assertEqual(nc2.getSkey(), (1,2,4,6,8))

    def test_getSkey(self,vertexValues,edges):
        nc1=NC((1,2,2,4,1,3,2,4,3))
        self.assertEqual(nc1.getSkey(), (2,1,2,3))
        nc2=NC((1,2,3,4,5,6,7,8,9))
        self.assertEqual(nc2.getSkey(), (3,5,7,9))

    def test_mergeVertexAxis(self,vertexValues,edges):
        nc=NC((1,2,3,4,5,6,7,8,9))
        self.assertEqual(NC.mergeVertexAxis(nc.getXkey(), nc.getSkey()), nc)

    def test_lexicographicNextValue(self,value,bound):
        
    def test_listOrder(self,list1, list2):

    def test_getVertexDifPosition(self,vertexValues):


if __name__ == '__main__':
    unittest.main()