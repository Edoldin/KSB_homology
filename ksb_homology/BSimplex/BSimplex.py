from comch import Simplex
from collections import defaultdict
import numpy.matlib
import numpy as np
class BSimplex(Simplex):

    def __init__(self, ptuple):
        """Initializes *self*.
        PARAMETERS
        ----------
        interable : :class:' ptuple'
            Used to create a :class:`tuple` of :class:`int`.
        EXAMPLE
        -------
        >>> print(Simplex((1,2,4)))
        >>> 
        (1,2,4)
        """
        if isinstance(ptuple, tuple):
            Simplex.__init__(ptuple)
        self._simplexsize=defaultdict(lambda: False)
        self._partial=defaultdict(lambda: False)
        self._mu=defaultdict(lambda: False)
    
    #-------- Private methods --------
    def _is_non_decreasing(ptuple):
        return ptuple.reduce(lambda a,b : b if b > a else 9999) != 9999

    def _is_subsecuence(simplex_base,simplex2, m, n):
        if len(simplex) == 0:
            return True
        if len(simplex_base) == 0:
            return False

        # If last characters of two 
        # strings are matching
        if string1[m-1] == string2[n-1]:
        return _is_subsecuence(string1, string2, m-1, n-1)
 
        # If last characters are not matching
        return _is_subsecuence(string1, string2, m, n-1)

    @staticmethod
    def _toSimplex(ptuple):
        if isinstance( ptuple, Simplex):
            return  ptuple
        elif isinstance( ptuple, tuple):
            return Simplex( ptuple)
        else:
            raise Exception(" ptuple type must be Simplex or tuple")

    #-------- Public methods --------
    def is_valid(self):
        if len(self)<=0 : return False
        if _is_non_decreasing(self) : return False
        #continue with more conditions
        return True

    def is_face(self,simplex):
        return _is_subsecuence(self, simplex, len(self), len(simplex))

    # _simplexsize -------------------------
    def get_ss(self, simplex):
        """I'm the 'simplex size' property."""
        return self._simplexsize[simplex]

    def set_ss(self, simplex, value):

        self.del_simplexsize[simplex]=value


    def del_ss(self, simplex):

        del self._simplexsize[simplex]

  # _partial ------------------------------
    def get_partial(self, simplex, i):

        """I'm the 'partial' property."""
        return self._partial[simplex,i]

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