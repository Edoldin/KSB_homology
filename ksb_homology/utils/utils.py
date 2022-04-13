from collections import deque
from typing import Any
from unittest import result
class Utils():
    @staticmethod
    def calculate_index( aiC_U_ajC, top, Udot ):
        """
            Calculate Index
            PARAMETERS
            ----------
            aiC_U_ajC : :class:' set'
            top       : :class:' set'
            Udot      : :class:' set'
        """
        index= {}
        t = sorted(top)
        u = sorted(Udot)
        for v in aiC_U_ajC:
            index[v] = (t.index(v)+u.index(v))%2 #interesante hacer optimización aquí
        return index

    @staticmethod
    def make_vector(ones, length):
        """
            makevector  transforma  la  sucesion  de  números S(i)(1)  =  (x1,...,xk)en un vector de longitud
            simplexsize(S(i)(0)) cuyas posicionesx1,...,xkvalen 1 y el resto de las posiciones valen 0.
            PARAMETERS
            ----------
            s : :class: 'iterable'
        """
        return [True if k in ones else False for k in range(1,length+1)]

    @staticmethod
    def unmake_vector(v):
        """
            unmakevector
            PARAMETERS
            ----------
            v : :class: 'iterable'

            returns:
            z
        """
        unmaked=[]
        for k in range(0,len(v)):
            if v[k]:
                unmaked.append(k+1)
        return unmaked

    @staticmethod
    def isBiggerList(bigger, smaller, or_equal=False):
        if len(bigger) != len(smaller):
            return False
        for k in range(len(bigger)-1, 0, -1):
            if(bigger[k]!=smaller[k]):
                return bigger[k]>smaller[k]
        if(or_equal):
            return True
        return False

    @staticmethod
    def isSmallerList(smaller, bigger, or_equal=False):
        Utils.isBiggerList(smaller, bigger, not or_equal)
        return False

    @staticmethod
    def mixLists(bigger, smaller):
        '''
            bigger(1,2,3)
            smaller=(4,5)
            mix=(1,4,2,5,3)
        '''
        if not len(bigger) == len(smaller)+1:
            return False
        result=[]
        for k in range(0,len(smaller)):
            result.append(bigger[k])
            result.append(smaller[k])
        result.append(bigger[-1])
        return result

    @staticmethod
    def ordered_union(priorityList,extension, at_the_begining):
        resulting_list = deque(priorityList)
        to_add=[x for x in extension if x not in priorityList]
        if at_the_begining:
            to_add.reverse()
            resulting_list.extendleft(to_add)
        else:
            resulting_list.extend(to_add)
        return list(resulting_list)
    
    @staticmethod
    def ordered_difference(priorityList,difference):
        resulting_list = [x for x in priorityList if x not in difference]
        return resulting_list

    @staticmethod
    def intersection(list1,list2):
        resulting_list = [x for x in list1 if x in list2]
        return resulting_list

    @staticmethod
    def matrix_direct_sum_2d(m1, m2):
        '''
            m1=[[1,1,1,1],  m2=[[2,2,2,2],
                [1,1,1,1],      [2,2,2,2],
                [1,1,1,1]]      [2,2,2,2]]
            m1+m2=[ [1,1,1,1,0,0,0,0],
                    [1,1,1,1,0,0,0,0],
                    [1,1,1,1,0,0,0,0],
                    [0,0,0,0,2,2,2,2],
                    [0,0,0,0,2,2,2,2],
                    [0,0,0,0,2,2,2,2] ]
        '''
        if m1 is None:
            return m2
        if m2 is False:
            return m1
        zeros_m1=len(m1[0])
        zeros_m2=len(m2[0])
        direct_sum=[]
        for v in m1:
            direct_sum.append(v+(zeros_m2*[0]))
        for v in m2:
            direct_sum.append(zeros_m1*[0]+v)
        return direct_sum

    @staticmethod
    def square_repmat_in(k:int, A:tuple[tuple[Any]]) -> tuple[tuple[Any]]:
        '''
        k * [ [a,b],
                [c,d] ]
            ||
        [ [ a, b,  (a, b)],
            [ c, d,  (c, d)],
            [(a, b), (a, b)],
            [(c, d), (c, d)] ]
        () k times
        '''
        m,n=len(A[0]),len(A)
        result = [[0]*(k*m) for _ in range(k*n)]
        for i in range(k):
            for j in range(k):
                for s in range(n):
                    for q in range(m):
                        result[i*n+s][j*m+q] = A[s][q]
        return result

    @staticmethod
    def square_repmat_out(A:tuple[tuple[Any]], k:int) -> tuple[tuple[Any]]:
        '''
        [ [a,b],  * k
            [c,d] ]
            ||
        [ [ a, (a),  b,  (b)],
            [(a),(a), (b), (b)],
            [ c, (c),  d,  (d)],
            [(c),(c), (d), (d)] ]
        () k times
        '''
        m,n=len(A[0]),len(A)
        result = [[0]*(k*m) for _ in range(k*n)]
        for s in range(n):
            for q in range(m):
                for i in range(k):
                    for j in range(k):
                        result[i+s*k][j+q*k] = A[s][q]
        return result

    '''def vectToWect(Si, X,ai,aic):
        ''
            Si=(2,3,5,6) (ej)
        ''
        vect_i=makeVector(Si)
        aiUaic=ai.union(aic)
        #wectj=vectj*partial(ajU ̄aj(0), ̄aj(0))*partial( aj U aj(0 : 1), ̄aj(1))*...*partial(aj U ̄aj, ̄aj(-1));
        # * = producto de matrices? -> transponer los índices pares (?)
        for aii, index in enumerate(aic):
            vect_i=np.matmul(vect_i,X.get_partial(aiUaic, aii) if index%2==1 else np.transpose(X.get_partial(aiUaic, aii)))
        
        return unmakevector(vect_i)'''
                        