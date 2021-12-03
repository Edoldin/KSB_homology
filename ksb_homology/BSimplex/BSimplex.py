from logging import error
from comch import Simplex
from collections import defaultdict
from collections.abc import Iterable
from ksb_homology.NCounter import NCounter as NC
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
            super().__init__(iterable)
        else:
            raise TypeError("BSimplex must be constructed with class iterable")
        #{simplex :int}
        self._simplexsize=defaultdict(lambda: 0)
        #{simplex, int :array}
        self._partial=defaultdict(lambda: False)
        #{simplex, simplex, int :array}
        self._mu=defaultdict(lambda: False)
        self._N=0


    @staticmethod
    def strictly_increasing(iterable):
        return all(x<y for x, y in zip(iterable, iterable[1:]))

    @staticmethod
    def Projective_plane():
        return BSimplex.Moore_space_Zn(2)
    
    @staticmethod
    def Moore_space_Zn(n):
        simplex=BSimplex((0,))
        simplex.set_simplexsize((),1)
        simplex.set_simplexsize((0,),1)
        simplex.set_partial((0,),0,n)
        return simplex

    @staticmethod
    def proyective_2planes_product_element():
        a=BSimplex((0,1))
        a.set_simplexsize((0,1),1)
        a.set_simplexsize((0,),1)
        a.set_simplexsize((1,),1)
        a.set_simplexsize((),1)

        a.set_partial((0,1),0,[2])
        a.set_partial((0,1),1,[2])
        a.set_partial((0,),0,[2])
        a.set_partial((1,),1,[2])

        a.set_mu((0,1),0,1,[1,3,2,4])
        return a

    def bijection(self, simplex, j, l, fi, ff):
        bot=set(simplex).difference({j,l})
        top=simplex
        nCounter1=self.nCounter(self, [simplex,bot.add(l),bot])
        nCounter2=self.nCounter(self, [simplex,bot.add(j),bot])
        def filterFunc(nC):
                if nC[0]==fi and nC[-1]==ff:
                    return True
                else:
                    return False
        filter(filterFunc, nCounter1)
        filter(filterFunc, nCounter2)
        if len(nCounter1)!=len(nCounter1):
            raise Exception("nCounters don't have the same lenght")
        biy={}
        mu=self.get_mu(simplex,j,l)
        for i, v in enumerate(nCounter1):
            biy[v]=nCounter2[mu[i]]
        return biy




    @staticmethod
    def is_subsecuence(simplex_base,simplex2, m, n):
        if len(simplex2) == 0:
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

    def path(self,bot, top, tuples=True):
        "fc: the standard path of simplices from top to bottom"
        bot=set(bot)
        top=set(top)
        way=top.difference(bot)
        path=[bot]
        for k in sorted(way,reverse=True):
            copy=path[-1].copy()
            copy.add(k)
            path.append(copy)
        path.reverse()
        #return inmutable tubles
        return path if not tuples else tuple(map(lambda x: tuple(x), path))

    def checkPartial(self, simplex1, simplex2, i1, i2):
        p1=self.get_partial(simplex1,i1)
        p2=self.get_partial(simplex2,i2)

    def nCounter(self, path):
        "fc: the standard path of vertices (simplex) from bottom to top. In tests: [(1),(1,3),(1,2,3)] or [(),(1),(0,1)]"
        vertexBounds=[]
        for simplex in path:
            "if simplex size not defined use 1"
            ss=self.get_simplexsize(tuple(simplex))
            if ss : vertexBounds.append(ss-1)
            else : return []
        "fc: the path of simplexsizes from top to bottom [2,3,2] o [2,2,2]"
        solution=[]
        "fc: this is the initialiation of xcounter"
        vertexValues=np.zeros(len(vertexBounds), dtype=int)
        "fc: Suppose vertexValues = [2,3,1] o [2,1,2] (arranged from top to bottom)"
        while not NC.arrayBiggerThan(vertexValues, vertexBounds):
            "fc: the (n-1)-list of all consecutive pairs of values [[2,3],[3,1]] o [[2,1],[1,2]] (arranged from top to bottom)"
            edges_vertex_value=[]
            while len(edges_vertex_value)+1 != len(vertexValues):
                edges_vertex_value.append((vertexValues[len(edges_vertex_value)],vertexValues[len(edges_vertex_value)+1]))
            "fc: the (n-1)-list of all bounds of the edges at the positions given by vertexValues. (not defined in the first test), [3,2]"
            edgesBounds=[]
            for posicion, parValue in enumerate(edges_vertex_value):
                partialSimplex=tuple(path[posicion])
                partialNumber=path[+posicion].difference(path[posicion+1]).pop()
                partial=self.get_partial(partialSimplex, partialNumber)
                if not partial.any(): return []
                edgesBounds.append(partial[parValue[1]][parValue[0]]-1)

            edges=np.zeros(len(vertexBounds)-1, dtype=int) #-k, dtype=int)
            "fc:produces scounters compatible with xcounter: [1,1], [1,2], [2,1], [2,2], [3,1], [3,3] and then merges them"
            while not NC.arrayBiggerThan(edges, edgesBounds):
                solution.append( NC.mergeVertexAxis(vertexValues, edges) )
                edges=NC.lexicographicNextValue(edges,edgesBounds)

            vertexValues=NC.lexicographicNextValue(vertexValues,vertexBounds)
        return solution

    def build_S(self):
        S=[]
        for ai, xi in self._simplexsize.items():
            simplexSizeS=tuple([*range(1,xi+1)])
            S.append((ai,simplexSizeS))
        return tuple(S)
    
    # _N -----------------------------------
    def get_N(self):
        '''
            máximo de todos los numeros que aparecen en los símpleces del BSimplex (no tiene porqué ser la dimensión del BS)
        '''
        N=0
        for key in self._simplexsize:
            for v in key:
                N = v if v>N else N
        return N

    # _simplexsize -------------------------
    def simplexRange(self):
        N=0
        for k in self:
            N = k if k>N else N
        return N 

    def get_simplexsize(self, simplex):
        """I'm the 'simplex size' property."""
        if isinstance(simplex, int):
            return self._simplexsize[tuple(simplex)]
        return self._simplexsize[simplex]

    def set_simplexsize(self, simplex, value):
        if isinstance(simplex, int):
            self._simplexsize[tuple(simplex)]=value
        elif isinstance(simplex, tuple):
            self._simplexsize[simplex]=value
        else:
            raise TypeError("simplex key can only be tuples or int")


    def del_simplexsize(self, simplex):

        del self._simplexsize[simplex]

  # _partial ------------------------------
    def get_partial(self, simplex, i):
        """I'm the 'partial' property."""
        partial = self._partial[simplex,i]
        if partial is False:
            l_simplex=list(simplex)
            if i in l_simplex:
                l_simplex.remove(i)
            if self._simplexsize[simplex] == 0 or self._simplexsize[tuple(l_simplex)] == 0:
                return 0
            else:
                raise Exception("partial of simplex", simplex, "should be explicitely defined")
        else:
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
        '''mu ha de ser una aplicacón que va de nCounters a nCounters'''
        self._mu[simplex,j,l]=value

    def del_mu(self, simplex, j, l):

        del self._mu[simplex,j,l]

    # Public Methods ------------------------


    #def checkMu(self, simplex1, simplex2, j1, j2, l1, l2):