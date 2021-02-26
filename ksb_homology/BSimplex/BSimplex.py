from comch import Simplex
from collections import defaultdict
from collections.abc import Iterable
import numpy.matlib
import numpy as np
class BSimplex(Simplex):

    def __init__(self, iterable):
        """Initializes *self*.
        PARAMETERS
        ----------
        interable : :class:' iterable'
            Used to create a :class:`tuple` of :class:`int`.
        EXAMPLE
        -------
        >>> print(Simplex((1,2,4)))
        >>> 
        (1,2,4)
        """
        if isinstance(iterable, Iterable):
            Simplex.__init__(iterable)
        else:
            raise TypeError("BSimplex must be constructed with class iterable")
        self._simplexsize=defaultdict(lambda: False)
        self._partial=defaultdict(lambda: False)
        self._mu=defaultdict(lambda: False)


    @staticmethod
    def strictly_increasing(iterable):
        return all(x<y for x, y in zip(iterable, iterable[1:]))

    @staticmethod
    def is_subsecuence(simplex_base,simplex2, m, n):
        if len(simplex) == 0:
            return True
        if len(simplex_base) == 0:
            return False

        # If last characters of two 
        # strings are matching
        if simplex_base[m-1] == simplex2[n-1]:
            return BSimplex.is_subsecuence(simplex_base, simplex2, m-1, n-1)

        # If last characters are not matching
        return BSimplex.is_subsecuence(simplex_base, simplex2, m, n-1)
    @staticmethod
    def ordered_union(simplex1,simplex2):
        return sorted(set(simplex1 + simplex2))

    @staticmethod
    def sub_sequences(iterable):
        simplex=set(iterable)
        return set([tuple(simplex.difference({k})) for k in simplex])


    #-------- Public methods --------
    def is_valid(self):
        if len(self)<=0 : return False
        if not BSimplex.strictly_increasing(self) : return False
        #continue with more conditions
        return True

    def is_face(self,simplex):
        return BSimplex.is_subsecuence(self, simplex, len(self), len(simplex))

    def checkPartial(self, simplex1, simplex2, i1, i2):
        p1=get_partial(simplex1,i1)
        p2=get_partial(simplex2,i2)

    def build_S(self):
        S=[]
        for ai, xi in self._simplexsize.items():
            for i in range(1,xi+1):
                S.append((ai,i))
        return tuple(S)

    # _simplexsize -------------------------
    def get_simplexsize(self, simplex):
        """I'm the 'simplex size' property."""
        return self._simplexsize[simplex]

    def set_simplexsize(self, simplex, value):

        self._simplexsize[simplex]=value


    def del_simplexsize(self, simplex):

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

    # Public Methods ------------------------


    #def checkMu(self, simplex1, simplex2, j1, j2, l1, l2):