from comch import Simplex
from collections import defaultdict
import numpy.matlib 
import numpy as np 
class BSimplex(Simplex):

    def __init__(self,iterable):
        """Initializes *self*.
        PARAMETERS
        ----------
        interable : :class:'iterable'
            Used to create a :class:`tuple` of :class:`int`.
        EXAMPLE
        -------
        >>> print(Simplex((1,2,4)))
        >>> 
        (1,2,4)
        """
        if isinstance(iterable, tuple):
            Simplex.__init__(iterable)
        self._partial=defaultdict(lambda: False)
        self._mu=defaultdict(lambda: False)
        print("BSimplex created",self)
    
    #-------- Private methods --------
    def _checkNonDecreasing(iterable):
        bool(lambda test_list: reduce(lambda i, j: j if 
                 i < j else 9999, test_list) != 9999)

    @staticmethod
    def _toSimplex(iterable):
        if isinstance(iterable, Simplex):
            return iterable
        elif isinstance(iterable, tuple):
            return Simplex(iterable)
        else:
            raise Exception("iterable type must be Simplex or tuple")

    #-------- Public methods --------
    def get_partial(self, simplex, i):

        """I'm the 'partial' property."""
        return self._partial.get([simplex,i],False)

    def set_partial(self, simplex, i, value):

        self._partial[simplex,i]=value


    def del_partial(self, simplex, i):

        del self._partial[simplex,i]
    
    # _mu --------------------------------
    def get_mu(self, simplex, j, l):
        """I'm the 'mu' property."""

        return self._mu[simplex,j,l]

    def set_mu(self, simplex, j, l, value):

        self.mu[simplex,j,l]=value

    def del_mu(self, simplex, j, l):

        del self._mu[simplex,j,l]


    def checkPartial(self, simplex1, simplex2, i1, i2):
        p1=get_partial(simplex1,i1)
        p2=get_partial(simplex2,i2)


    #def checkMu(self, simplex1, simplex2, j1, j2, l1, l2):