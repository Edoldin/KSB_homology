from logging import error
from comch import Simplex
from more_itertools import powerset
from comch.symmetric import SymmetricGroupElement
from collections import defaultdict
#from collections.abc import Iterable
from ksb_homology.Double_seq import Double_seq as D_SEQ
from ksb_homology.Utils import Utils as ut
import numpy as np

class BurnsideCube():

    def __init__(self, N):
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
        #{simplex :int}
        self._size=defaultdict(lambda: 0)
        #{simplex, int :array}
        self._partial=defaultdict(lambda: False)
        #{simplex, simplex, int :array}
        # mu es una matriz de permutaciones
        # 
        self._mu=defaultdict(lambda: False)
        '''
            máximo de todos los numeros que aparecen en los símpleces del BurnsideCube (no tiene porqué ser la dimensión del BS)
        '''
        self._N=N


    @staticmethod
    def strictly_increasing(iterable):
        return all(x<y for x, y in zip(iterable, iterable[1:]))

    '''
        The projective plane: Define a 1-dimensional Burnside cube F:
        • F.size() = 1, F.size(1) = 1
        • F.partial(1,1) = [2]
    '''
    @staticmethod
    def Projective_plane():
        simplex=BurnsideCube(1)
        simplex.set_size((),1)
        simplex.set_size((0,),1)
        simplex.set_partial((0,),0,[[2]])
        return simplex

    @staticmethod
    def Trefoil_knot():
        simplex=BurnsideCube(3)
        simplex.set_size((),3)
        simplex.set_size((0,),2)
        simplex.set_size((1,),2)
        simplex.set_size((2,),2)
        simplex.set_size((0,1),1)
        simplex.set_size((0,2),1)
        simplex.set_size((1,2),1)
        simplex.set_size((0,1,2),1)

        simplex.set_partial((0,1,2),0,[[1]])
        simplex.set_partial((0,1,2),1,[[1]])
        simplex.set_partial((0,1,2),2,[[1]])
        
        simplex.set_partial((0,1),0,[[1],[1]])
        simplex.set_partial((0,1),1,[[1],[1]])
        simplex.set_partial((0,2),0,[[1],[1]])
        simplex.set_partial((0,2),2,[[1],[1]])
        simplex.set_partial((1,2),1,[[1],[1]])
        simplex.set_partial((1,2),2,[[1],[1]])

        simplex.set_partial((0,),0,[[1,0],[0,1],[1,0]])
        simplex.set_partial((1,),1,[[1,0],[0,1],[1,0]])
        simplex.set_partial((2,),2,[[1,0],[0,1],[1,0]])
        return simplex

    '''
        The empty cube: Define an n-dimensional Burnside cube F:
        • F.size(vertex) = 0 for all vertex
        • All the matrices F.partial and F.mu are empty i.e., of size 0 x 0.
    '''
    @staticmethod
    def Empty_cube(n:int):
        vertexes=BurnsideCube.vertexes(n)
        simplex=BurnsideCube(n)
        for v in vertexes:
            simplex.set_size(v,0)
        return 

    '''
       The standard simplex: Define an n-dimensional Burnside cube F:
        • F.size(vertex) = 1 for all vertex
        • F.partial(vertex,i) = [1] for all vertex and all i ∈ vertex.
        • F.mu(vertex,i,j) = [(1)] for all vertex and all i < j ∈ vertex.
    '''
    @staticmethod
    def Standar_simplex(n:int):
        vertexes=BurnsideCube.vertexes(n)
        simplex=BurnsideCube(n)
        for v in vertexes:
            simplex.set_size(v,1)
            for i in v:
                simplex.set_partial(v,i,[[1]])
                for j in range(i+1,n):
                    simplex.set_mu(v,i,j,np.array([[1]]))
        return simplex

    '''
    old test cases
        
    @staticmethod
    def Projective_plane():
        return BurnsideCube.Moore_space_Zn(2)
    
    @staticmethod
    def Moore_space_Zn(n):
        simplex=BurnsideCube((2))
        simplex.set_size((),1)
        simplex.set_size((0,),1)
        simplex.set_partial((0,),0,n)
        return simplex

    @staticmethod
    def proyective_2planes_product_element():
        a=BurnsideCube((0,1))
        a.set_size((0,1),1)
        a.set_size((0,),1)
        a.set_size((1,),1)
        a.set_size((),1)

        a.set_partial((0,1),0,[2])
        a.set_partial((0,1),1,[2])
        a.set_partial((0,),0,[2])
        a.set_partial((1,),1,[2])

        a.set_mu((0,1),0,1,[1,3,2,4])
        return a
    '''
    
    @staticmethod
    def vertexes(N:int):
        return powerset(range(1,N))
        
    @staticmethod
    def is_subsecuence(simplex_base,simplex2, m, n):
        if len(simplex2) == 0:
            return True
        if len(simplex_base) == 0:
            return False

        # If last characters of two 
        # strings are matching
        if simplex_base[m-1] == simplex2[n-1]:
            return BurnsideCube.is_subsecuence(simplex_base, simplex2, m-1, n-1)

        # If last characters are not matching
        return BurnsideCube.is_subsecuence(simplex_base, simplex2, m, n-1)

    @staticmethod
    def ordered_union(simplex1,simplex2):
        return sorted(set(simplex1 + simplex2))

    @staticmethod
    def sub_sequences(iterable):
        sub_sequence=set()
        for k in iterable:
            simplex=set(iterable)
            simplex.remove(k)
            sub_sequence.add(tuple(simplex))
        return sub_sequence

    def Dual(self):
        '''
        The dual of a Burnside cube: Given an n-dimensional cube F, define its dual cube D as follows
        (here vertex* denotes the complement of vertex in {1, 2, . . . , n}).
            D.size(vertex) = F.size(vertex*)
            D.partial(vertex,i) = F.partial(vertex* U {i}, i)ᵀ
            D.mu(vertex,i,j) = F.mu(vertex* U {i,j}, i,j)ᵀ
        '''
        N=len(self)
        total=range(0, N)
        dual= BurnsideCube(N)
        for vertex in self._size:
            vertex_complement=tuple(set(total).difference(set(vertex)))
            dual.set_size(vertex_complement,self.get_size(vertex))
        for key in self._partial:
            # key = (vertex, i)
            v_complement=set(total).difference(set(key[0]))
            v_complement.add(key[1])
            vertex_complement=tuple(v_complement)
            partial_transpose=tuple(zip(*self._partial[key]))
            dual.set_partial(vertex_complement, key[1], partial_transpose)
            
        for key in self._mu:
            # key = (vertex, i, j)
            v_complement=set(total).difference(set(key[0]))
            v_complement.add(key[1],key[2])
            vertex_complement=tuple(v_complement)
            mu_transpose=tuple(zip(*self._mu(key)))
            dual.set_mu(vertex_complement, key[1], key[2], mu_transpose)

        return dual

    def bijection(self, simplex, j, l, fi, ff):
        bot=set(simplex).difference({j,l})
        double_seq1=self.double_seq(self, [simplex,bot.add(l),bot])
        double_seq2=self.double_seq(self, [simplex,bot.add(j),bot])
        def filterFunc(nC):
            if nC[0]==fi and nC[-1]==ff:
                return True
            else:
                return False
        filter(filterFunc, double_seq1)
        filter(filterFunc, double_seq2)
        if len(double_seq1)!=len(double_seq1):
            raise Exception("double_seqs don't have the same lenght")
        biy={}
        mu=self.get_mu(simplex,j,l)
        for i, v in enumerate(double_seq1):
            biy[v]=double_seq2[mu[i]]
        return biy


    '''
    comprobar que en todos los setters los vértices que se pasan son subconjuntos de el símplice de BurnsideCube (0,1,...,N-1)
    (que tiene valores únicos y que todos esos valores son menores que N) (indizar por sets)
    '''

    def is_vertex_valid(self,vertex):
        #empty must be valid, for each v in vertex v  is in {0,...,N-1}
        for k in vertex:
            if k > len(self)-1 or k<0:
                return [False,"Vertex can not have any point upper to the BurnsideCube lenght"]
        if len(set(vertex)) is not len(vertex):
            return [False,"Vertex can not contain any repeated element"]
        return True
        
    def is_valid(self):
        if len(self)<=0 : return False
        vertexes=BurnsideCube.vertexes(len(self))
        '''
            For every vertex of the cube, a finite set.
            For every subset vertex of [n], a natural number F.size(vertex).
        '''
        for v in vertexes:
            if self.get_size(v) < 0 :
                return False
        '''
            For every edge of the cube, a correspondence between the sets assigned to
            their vertices.
            For every subset vertex of [n] and every element i ∈ vertex, a
            matrix F.partial(vertex,i) of natural numbers of size F.size(vertex)xF.size(vertex\{i}).
        '''
        for v in vertexes:
            sizeV=self.get_size(v.difference())
            sizeV=self.get_size(v)
            for i in v:
                partial=self.get_partial(v,i)
                if not partial:
                    return False
                if len(partial) != sizeV:
                    return False
                
        '''
            For every 2-dimensional face, a 2-morphism.
            For every subset vertex of {1, . . . , n} and every two elements
            i, j ∈ vertex with i < j, a matrix of permutations of size F.size(vertex\{i,j})xF.size(vertex).
            The (i, j)th permutation is a permutation of
            the cardinal given by the (i, j)th entry of the composite matrix

            F.partial(vertex,i) · F.partial(vertex\{i},j}). This ma-
            trix of permutations is called F.mu(vertex,i,j).
        '''
        return True

    def is_face(self,simplex):
        return BurnsideCube.is_subsecuence(self, simplex, len(self), len(simplex))

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

    '''
        double_seq is just for an internal propouse do not use it
        Cambiar double_seq -> Double_SEQ
        edges -> seq_edges (s_edges)
        vertex_values -> seq_vertex (s_vertex)
    '''
    def double_seq(self, path):
        "fc: the standard path of vertices (simplex) from bottom to top. In tests: [(1),(1,3),(1,2,3)] or [(),(1),(0,1)]"
        seq_vertex_bounds=[]
        for simplex in path:
            "if simplex size not defined use 0"
            ss=self.get_size(tuple(simplex))
            if ss : seq_vertex_bounds.append(ss-1)
            else : return []
        "fc: the path of simplexsizes from top to bottom [2,3,2] o [2,2,2]"
        solution=[]
        "fc: this is the initialiation of xcounter"
        seq_vertex=np.zeros(len(seq_vertex_bounds), dtype=int)
        "fc: Suppose seq_vertex = [2,3,1] o [2,1,2] (arranged from top to bottom)"
        while not D_SEQ.arrayBiggerThan(seq_vertex, seq_vertex_bounds):
            "fc: the (n-1)-list of all consecutive pairs of values [[2,3],[3,1]] o [[2,1],[1,2]] (arranged from top to bottom)"
            edges_vertex_value=[]
            while len(edges_vertex_value)+1 != len(seq_vertex):
                edges_vertex_value.append((seq_vertex[len(edges_vertex_value)],seq_vertex[len(edges_vertex_value)+1]))
            "fc: the (n-1)-list of all bounds of the edges at the positions given by seq_vertex. (not defined in the first test), [3,2]"
            seq_edgesBounds=[]
            for posicion, parValue in enumerate(edges_vertex_value):
                partialSimplex=tuple(path[posicion])
                partialNumber=path[+posicion].difference(path[posicion+1]).pop()
                partial=self.get_partial(partialSimplex, partialNumber)
                if not partial.any(): return []
                seq_edgesBounds.append(partial[parValue[1]][parValue[0]]-1)

            seq_edges=np.zeros(len(seq_vertex_bounds)-1, dtype=int) #-k, dtype=int)
            "fc:produces scounters compatible with xcounter: [1,1], [1,2], [2,1], [2,2], [3,1], [3,3] and then merges them"
            while not D_SEQ.arrayBiggerThan(seq_edges, seq_edgesBounds):
                solution.append( D_SEQ.merge_sVertexEdges(seq_vertex, seq_edges) )
                seq_edges=D_SEQ.lexicographicNextValue(seq_edges,seq_edgesBounds)

            seq_vertex=D_SEQ.lexicographicNextValue(seq_vertex,seq_vertex_bounds)
        return solution

    def build_S(self):
        S=[]
        for ai, xi in self._size.items():
            simplexSizeS=tuple([*range(1,xi+1)])
            S.append((ai,simplexSizeS))
        return tuple(S)

    # _size -------------------------
    def __len__(self):
        return self._N

    def simplexRange(self):
        N=0
        for k in self:
            N = k if k>N else N
        return N 

    def get_size(self, vertex):
        """I'm the 'vertex size' property."""
        if isinstance(vertex, int):
            return self._size[tuple(vertex)]
        return self._size[vertex]

    def set_size(self, vertex : tuple, size:  int):
        '''
            >>> burnside_cube.set_size([1,2,3], 5)
        '''
        if(self.is_vertex_valid(vertex) is not True):
            raise Exception("vertex not valid",self.is_vertex_valid(vertex)[1])
        if not isinstance(size, int) or size<0:
            raise TypeError("Size must be a non negative integer")

        if isinstance(vertex, int):
            self._size[tuple(vertex)]=size
        elif isinstance(vertex, tuple):
            self._size[vertex]=size
        else:
            raise TypeError("Vertex key can only be tuples or int")

    def del_size(self, vertex):
        del self._size[vertex]

    # _partial ------------------------------
    def get_partial(self, vertex:tuple[int], i:int):
        """I'm the 'partial' property."""
        partial = self._partial[vertex,i]
        if partial is False:
            childVertex=list(vertex)
            if i in childVertex:
                childVertex.remove(i)
            else:
                raise Exception("When you get a partial, i must be inside the vertex you pass")

            if self._size[vertex] == 0 or self._size[tuple(childVertex)] == 0:
                return 0
            else:
                raise Exception("partial of simplex", vertex, i, "should be explicitely defined")
        else:
            return self._partial[vertex,i]

    def set_partial(self, vertex:tuple[int], i:int, matrix:tuple[tuple[int]]):
        '''
            matrix tiene que tener el tamaño:
                (self.get_size(vertex))x(self.get_size(vertex.remove(i)))
        '''
        if(i not in vertex):
            raise Exception("i must be in vertex")
        if(not self.is_vertex_valid(vertex)):
            raise Exception("vertex not valid")
        matrixM=self.get_size(vertex)
        matrixN=self.get_size(tuple(set(vertex).difference({i})))
        if all(len(column) is matrixM for column in matrix) and len(matrix) is matrixN:
            self._partial[vertex,i]=matrix
        else:
            raise Exception("value assigned to partial %s i:%x must be %xx%x but it's %xx%x"%(",".join(vertex), i, matrixN, matrixM, len(matrix[0]), len(matrix)))

    def del_partial(self, vertex, i):
        del self._partial[vertex,i]

    # _mu --------------------------------
    def get_mu(self, simplex, j, l):
        """I'm the 'mu' property."""

        return self._mu[simplex,j,l]

    def set_mu(self, vertex, j, l, matrix):
        '''mu ha de ser una aplicacón que va de double_seqs a double_seqs'''
        ''' Buscar librería de matrices y añadir comprobación
            matrix tiene que tener el tamaño:
                (self.get_size(vertex))x(self.get_size(vertex.remove(j,l)))
        '''
        if(not self.is_vertex_valid(vertex)):
            raise Exception("vertex not valid")
        matrixN=self.get_size(vertex)
        matrixM=self.get_size(tuple(set(vertex).difference({j, l})))
        if all(len(column) is matrixM for column in matrix) and len(matrix) is matrixN:
            if all(isinstance(symmetric, SymmetricGroupElement) for column in matrix for symmetric in column):
                self._mu[vertex,j,l]=matrix
            else:
                raise Exception("value assigned to mu must be an tuple of permutations (comch.symmetric.SymmetricGroupElement)")
        else:
            raise Exception("value assigned to partial must be a 2 dimensional",(matrixN,matrixM))
        
        #for x in matrix:
        #    for y in x:
        #        if not isinstance(matrix[x,y], SymmetricGroupElement):
        #            raise Exception("value assigned to mu must be an tuple of permutations (comch.symmetric.SymmetricGroupElement)")
        #self._mu[simplex,j,l]=matrix

    def del_mu(self, vertex, j, l):

        del self._mu[vertex,j,l]

    def is_equal(self,equal):
        if len(self) is not len(equal):
            return False
        for i in self._size:
            if self._size[i] is not equal._size[i]:
                return False
        for i in self._partial:
            if self._partial[i] is not equal._partial[i]:
                return False
        for i in self._mu:
            if self._mu[i] is not equal._mu[i]:
                return False
        return True
    
    def Union(self,other):
        '''
            Given two Burnside cubes F, G
            of dimensions m and n, define their union H as:
        '''
        union=BurnsideCube(len(self)+len(other))
        '''
            H.size(vertex) = F.size(vertex) + G.size(vertex) (if one of these
            quantities is not defined, set it to zero).
        '''
        for i in self._size:
            union.set_size(i,self._size[i]+other._size[i])
        for i in other._size:
            if union._size[i] == 0:
                union.set_size(i,self._size[i]+other._size[i])
        '''
            H.partial(vertex,i) = F.partial(vertex,i)⊕G.partial(vertex,i)
        '''
        for key in self._partial:
            union.set_partial(key[0], key[1], ut.matrix_direct_sum_2d(self._partial[key], other._partial[key]))
        for key in other._partial:
            if union._partial[i] is False:
                union.set_partial(key[0], key[1], ut.matrix_direct_sum_2d(self._partial[key], other._partial[key]))
        '''
            H.mu(vertex,i,j) = F.partial(vertex,i)⊕G.partial(vertex,i)
        '''
        for key in self._mu:
            union.set_mu(key[0], key[1], key[2], ut.matrix_direct_sum_2d(self._mu[key], other._mu[key]))
        for key in other._mu:
            if union._mu[i] is False:
                union.set_mu(key[0], key[1],  key[2], ut.matrix_direct_sum_2d(self._mu[key], other._mu[key]))
        return union

    def Join(self,other):
        '''
            The join of two Burnside cubes. Here are a couple of definitions that we
            will need later:
            Observe first that every number α between 0 and mn-1 can be written uniquely
            as am + b with 0 ≤ a < n and 0 ≤ b < m (a and b are the quotient and remainder
            obtained after dividing α by m).
        '''
        '''
            Given a matrix A of size m x n and a number k, define the matrices of size km x kn as follows:
                right: (k · A)[ak + q, bk + s] = A[q, s]
                left:  (A · k)[ak + q, bk + s] = A[a, b]
        '''

        def matrix_join_multiplication(A:tuple[tuple[int]], B:tuple[tuple[int]]) -> tuple[tuple[int]]:
            '''
            Given two matrices A and B of size m x n and p x q respectively, define the
            permutation matrix A * B of size mp x nq as follows:
                A * B[rp + s, tq + u] = tau(A[r, t], B[s, u]) for r < m, s < p, t < n, u < q
            '''
            m,n=len(A[0]),len(A)
            p,q=len(B[0]),len(B)
            result = [[0]*(m*p) for _ in range(n*q)]
            
            def tau(a:int,b:int) -> list[int]:
                '''
                Given two numbers (a, b), define the permutation tau(a,b) of {0, 1, . . . , ab - 1} as
                tau(a, b)(ra + s) = sb + r for r < b and s < a
                '''
                permutation=[0]*(a*b-1)
                for r in range(b):
                    for s in range(a):
                        permutation[r*a+s]=s*b+r
                return permutation

            for r in range(m):
                for s in range(p):
                    for t in range(n):
                        for u in range(q):
                            result[r*p+s][t*q+u] = tau( A[r,t], B[s,u])

            return result
        '''
            Join of two cubes: Given two cubes F, G of dimensions m and n,
            define their join J = F * G, which is a cube of dimension m + n as follows.
        '''
        m=len(self)
        join=BurnsideCube(m+len(other))
        vertexes = powerset(list(range(len(join))))
        '''
            J.size(vertex) = F.size(vertex1)·G.size(vertex2)
        '''
        for vertex in vertexes:
            vertex1=tuple([v for v in vertex if v < len(self)])
            vertex2=tuple([v-len(other) for v in vertex if v >= len(other)])
            join.set_size(vertex,self.get_size(vertex1)*other.get_size(vertex2))
            '''
                J.partial(vertex,i) =
                    F.partial(vertex,i) = F.partial(vertex1,i)·G.size(vertex2) if i < m
                    F.partial(vertex,i) = F.size(vertex1)·G.partial(vertex2,i) if i ≥ m
            '''
            for i in vertex:
                if i < m:
                    partial=ut.square_repmat_out(self.get_partial(vertex1,i),other.get_size(vertex2))
                else:
                    partial=ut.square_repmat_in(self.get_size(vertex1), other.get_partial(vertex2,i-m))
                join.set_partial(vertex,i,partial)
                ''' 
                    J.mu(vertex,i,j) =
                        F.mu(vertex1,i,j)·G.size(vertex2) if i, j < m
                        F.size(vertex1)·G.mu(vertex2,i-m,j-m) if i, j ≥ m
                        F.partial(vertex1,i)*G.partial(vertex2,j-m) if i < m, j ≥ m
                '''
                for j in [v for v in vertex if v > i]:
                    mu=[]
                    if i < m and j < m:
                        mu=ut.square_repmat_out( self.get_mu(vertex1,i,j), other.get_size(vertex2) )
                    if i >=m and j >=m:
                        mu=ut.square_repmat_in( self.get_size(vertex1), other.get_mu(vertex2,i-m,j-m) )
                    if i < m and j > m:
                        mu=matrix_join_multiplication( self.get_partial(vertex1,i), other.get_partial(vertex2,j-m))
                    join.set_mu(vertex, i, j, mu)

        return 1