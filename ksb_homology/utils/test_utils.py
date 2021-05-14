import sys, os
ksb_homology_path_list=os.path.dirname(os.path.realpath(__file__)).split("\\")[0:-2]
ksb_homology_path= "\\".join(ksb_homology_path_list)
if ksb_homology_path not in sys.path:
    sys.path.append(ksb_homology_path)

import unittest
from ksb_homology.Utils import Utils as ut

class BSimplexTest(unittest.TestCase):

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

    def test_ordered_intersection(self):
        priorityList=[1,2,4,3,5]
        intersection=[1,2,3]
        self.assertEqual(ut.ordered_intersection(priorityList,intersection), [4,5])
        priorityList=[4,3,5,1,2]
        self.assertEqual(ut.ordered_intersection(priorityList,intersection), [4,5])
        intersection=[3]
        self.assertEqual(ut.ordered_intersection(priorityList,intersection), [4,5,1,2])
        intersection=[5,1,2]
        self.assertEqual(ut.ordered_intersection(priorityList,intersection),  [4,3])


if __name__ == '__main__':
    unittest.main()