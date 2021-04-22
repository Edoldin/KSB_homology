from comch import Simplex
from collections import defaultdict
from collections.abc import Iterable
import numpy.matlib
import numpy as np
import bisect
import itertools

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
        #{simplex :int}
        self._simplexsize=defaultdict(lambda: False)
        #{simplex, int :array}
        self._partial=defaultdict(lambda: False)
        #{simplex, simplex, int :array}
        self._mu=defaultdict(lambda: False)
        self._N=0


    @staticmethod
    def strictly_increasing(iterable):
        return all(x<y for x, y in zip(iterable, iterable[1:]))
    
    @staticmethod
    def proyective_2planes_product_element():
        a=BS((0,1))
        a.set_simplexsize((0,1),1)
        a.set_simplexsize((0),1)
        a.set_simplexsize((1),1)
        a.set_simplexsize((),1)

        a.set_partial((0,1),0,[2])
        a.set_partial((0,1),1,[2])
        a.set_partial((0),0,[2])
        a.set_partial((1),1,[2])

        a.set_mu((0,1),0,1,[1,3,2,4])
        return a

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

"fc: the standard path of simplices from bottom to top"
    def path(self,bottom, top): 
        print("bot,top",bottom, top)
        way=set(top).difference(set(bottom))
        way=sorted(way, reverse=True)
        path=[bottom]
        for k in way:
            copy=list(path[-1])
            bisect.insort(copy, k)
            path.append(tuple(copy))
        path.append(top)
        print("path",path)
        return tuple(path)

    def checkPartial(self, simplex1, simplex2, i1, i2):
        p1=get_partial(simplex1,i1)
        p2=get_partial(simplex2,i2)

    def nCounter(self, bot, top):

        def mergeVertexAxis(vertexValues,edges):
            vector=[]
            for e,i in enumerate(edges):
                vector.append(vertexValues[i],e)
            vector.append(vertexValues[-1])
            return vector

        def lexicographicNextValue(value,bound):
            k=len(bound)-1
            value[k]+=1
            while bound[k]<value[k] and k<0:
                value[k]=1
                k-=1
                value[k]+=1
            return value

        def solutionOrder(list1, list2):
            if list1[0]!=list2[0]:
                return list1[0]>list2[0]
            if list1[1]!=list2[1]:
                return list1[1]>list2[1]
            #list1 and list2 have the same length
            k=2
            while k<len(list1):
                if list1[k]!=list2[k]:
                    return list1[0]>list2[0]
                k+=1
        def getVertexDifPosition(vertexValues):
            for v,k in enumerate(vertexValues):
                if(v!=1):
                    return k
            return 0

        path=self.path(bot,top)  "fc: the standard path of vertices (simplex) from bottom to top. In tests: [(1),(1,3),(1,2,3)] or [(),(1),(0,1)]"
        vertexBounds=[]
        for simplex in path:
            "if simplex size not defined use 1"
            vertexBounds.append(self.get_simplexsize(simplex) or 0)#el 0 es un valor válido
        vertexBounds.reverse()    "fc: the path of simplexsizes from top to bottom [2,3,2] o [2,2,2]"
        solution=[]
        vertexValues=np.ones(len(vertexBounds), dtype=int) "fc: this is the initialiation of xcounter"
        # this is inefficient since i'm getting all partial for each vertex iteration
        # and the partial only changes when a vertex changes so i could only get once
        # I'm also not generating the nCounter in the lexicographic order
        
        # si hay algún 0 retornar una lista vacía
        #ver que si hay algún 0 no entre en un bucle infinito
        while not np.array_equal(vertexValues, vertexBounds): "fc: Suppose vertexValues = [2,3,1] o [2,1,2] (arranged from top to bottom)"
            edges_vertex_value=[]   "fc: the (n-1)-list of all consecutive pairs of values [[2,3],[3,1]] o [[2,1],[1,2]] (arranged from top to bottom)"
            while len(edges_vertex_value)+1 != len(vertexValues):
                edges_vertex_value.append((vertexValues[len(edges_vertex_value)],vertexValues[len(edges_vertex_value)+1]))
            
            edgesBounds=[]      "fc: the (n-1)-list of all bounds of the edges at the positions given by vertexValues. (not defined in the first test), [3,2]"      
            for parValue, posicion in enumerate(edges_vertex_value):
                edgesBounds.append( self.get_partial(path[-posicion], path[-posicion-1].diference(path[-posicion-2])[parValue[0]][parValue[1]] ))
# OJO: si alguno de los edgesbounds es cero, entonces no se debe añadir nada.
            edges=np.ones(len(vertexBounds)-1, dtype=int) #-k, dtype=int) 
            while not np.array_equal(edgesBounds, edges): "fc:produces scounters compatible with xcounter: [1,1], [1,2], [2,1], [2,2], [3,1], [3,3] and then merges them"
                solution.append(mergeVertexAxis(vertexValues, edges))
                edges=lexicographicNextValue(edges,edgesBounds)
# OJO: Aquí debajo, nC debería ser solution 
            nC.append(tuple(vertexValues))
            vertexValues=lexicographicNextValue(vertexValues,vertexBounds)

        return solution.sort(key=solutionOrder)

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
        for k in self:
            N = k if k>N else N
        return N

    # _simplexsize -------------------------
    def simplexRange(self):
        N=0
        for k in self:
            N = k if k>N else N
        return N 

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