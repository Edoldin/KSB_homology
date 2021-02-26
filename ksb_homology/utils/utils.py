from collections import defaultdict
from ksb_homology.BSimplex import BSimplex as BS


def calculateIndex(aiC_U_ajC,top,Udot):
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
        index[v] = t.index(v)+u.index(v)
    return index


def kth_stennrod_square(k,X,S):
    '''
        k>0
        X
        S a collection of pairs (ai,xi)
        ai is a simplex in X
        1<xi<simplexsize(ai)
    '''
    T=defaultdict(lambda: False)
    for i in range(0,len(S)):
        for j in range(i,len(S)):
            ai = set(S[i][0])
            aj = set(S[j][0])
            bottom = ai.union(aj)
            #d? not defined
            rep = d+k+1-len(ai.union(aj))
            if rep<0:
                #Uddot? it's a simplex of length rep so is this all the subsimplex of lenght rep in {0,..,n}?
                #n?
                for Uddot in set(range(0,n)).difference(bottom):
                    top = aiUaj.union(Uddot)
                    aiC = ai.difference(aj)
                    ajC = aj.difference(ai)
                    Udot = Uddot.union(aiC).union(ajC)
                    index = calculateIndex(aiC_U_ajC,top,Udot)
                    if (v in aiC and index[v] == 0) or (v in ajC and index[v] == 1):
                        vect_i
                        vect_j
                        wect