from collections import defaultdict
from ksb_homology.BSimplex import BSimplex as BS
from itertools import combinations
import numpy as np


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

def make_vector(ones, length):
    """
        makevector  transforma  la  sucesion  de  números S(i)(1)  =  (x1,...,xk)en un vector de longitud
        simplexsize(S(i)(0)) cuyas posicionesx1,...,xkvalen 1 y el resto de las posiciones valen 0.
        PARAMETERS
        ----------
        s : :class: 'iterable'
    """
    return [True if k in ones else False for k in range(1,length)]

def unmake_vector(v):
    """
        unmakevector
        PARAMETERS
        ----------
        v : :class: 'iterable'

        returns:
        z
    """
    return [k if v for k in range(1,v.length)]

def isBiggerList(bigger, smaller):
    if not len(bigger) == len(smaller)) return False
    for k in range(len(bigger)-1, 0, -1):
        if(bigger[k]<smaller[k]) return False
        if(bigger[k]>smaller[k]) return True
    return False
def mixLists(bigger, smaller):
    '''
        bigger(1,2,3)
        smaller=(4,5)
        mix=(1,4,2,5,3)
    '''
    if not len(bigger) == len(smaller)+1 return False
    result=[]
    for k in range(0,len(smaller)):
        result.append(bigger[k])
        result.append(smaller[k])
    result.append(bigger[-1])
    return result

def add(T,pair):
    """
        add pair to T
        -if T(c) is not defined T(c)=z (c,z).
        -if T(c) is defined T(c)=simetric difference of T(c) and z.
        PARAMETERS
        ----------
        T :    :class: 'defaultdict(lambda: False)'
        pair : :tuple: '(c,z) where c is a tuble and z is a set or a number'
    """
    if T[pair(0)]==False):
        T[pair(0)]=pair(1)
    else:
        T[pair(0)]=T[pair(0)] ^ pair(1)
#total[k]=((xc,sc),(yc,tc)) implementar clase NCounter() con los métodos:
    #total[k][0]=lista intercalada xcounter
    #total[k][1]=lista intercalada ycounter
# getXkey(total[1])
# getSkey(total[1])
# total[1]

def smash(X, top, bottom, x, y ):
    n=len(top)-len(bottom)
    #uddot are the tags of the edges and n is the number of edges
    uddot=top.difference(bottom)
    #path from top to bottom sigma contains all simplex in the path
    sigma=X.path(bottom,top).reverse()
    #sk is a simplex in the tree
    for sk, k in enumerate(sigma):
        #la comprobación xcounter(k+1) > ycounter(k+1) no es siempre falsa?  xcounter==ycounter
        #                           ||
        #lo mismo para xcounter(k+1) = ycounter(k+1) && scounter(k) > tcounter(k)
        # xCounter= {
        #    lista con longitud n que no coincide con el simplex size de sk en X
        #    cada una de las entradas tiene que estar acotada con el simplex size del símplice
        #    n=5; top= (1,2,3,4,5,6,7,8,9) bot= (1,2,3,4) X.ss(top)=5
        #    xCounter(0)=[[1,2,3,4,5],[],[],[],[]]
        # }
        #for i in range(0,n):#mirar video
        nCounters=X.nCounter(top,bottom) #todas las posibles xcounters scounters
        total=[]
        for nC1 in range(0,nCounters): # Si n = 3 xCounter=(1,1,1)=xCounters[0]
            for nC2 in range(nC1+1,nCounters):
                total.append((nC1,nC2)) #nC1 (xCounter, sCounter) nC2 (Ycounter, tCounter)

        global_smash(top, bot, tuple(total))

def global_smash(top, bot, total):
    paralel=[[]]
    uddot=sorted(set(top).difference(set(bot)))
    n=len(uddot)
    circle=[]
    circle.append(uddot)
    remaining=[[]]
    for l in range(1:n-1):
        parallel[l]=circ(0)[0:l-1]
        circ[l]=circ(0)[l-1:n]
        remaining[l]=[]

    stop=false
    level=-1
    pivot=0
    parpivot=0
    #total will be an inmutable tuple while total adapted will change.
    total_adapted=list(total)
    result=global_check(total, total_adapted, parallel, circ, remain) #returns a bool
    # increase will modify parallel, circ, remain, level, pivot, stop
    pivot, parpivot, level, stop = increase(parallel, circ, remain)
    while not stop:
        #global_change only modifies total_adapted
        global_change(total, total_adapted, level, pivot, parpivot)
        result+=global_check(total, total_adapted, parallel, circ, remain)#returns a bool
        pivot, parpivot, level, stop=increase(parallel, circ, remain)
    return result

#nc=((1,2,4,3,7),(1,3,2,9,9)),...
#ncAdapted=total_adapted
#nCAdapted=(((1,2,4,3,7),(1,2,4,3,7),(1,3,2,9,9), (1,3,2,9,9)))
#n va a ser el numero de aristas nCounter tendrá longitud 2n+1
def global_check(total, total_adapted, parallel, circ):
    output=False
    n=(len(total)-1)/2
    for xcsc,yctc in total_adapted:
        for l in range(0,n):
            k=len(parallel[l])
            m=len(circ[l])
            limit1=2*k+2
            limit2=2*k+2:2*k+2*m+2
            if xcsc(l)[0:limit1] != ycrc(l)[0:limit1] or xcsc(l)[limit1:limit2] >= yctc(l)[limit1:limit2]:
                return output
        if l=n-1:
            output=True+output
    return output

def global_change(total, total_adapted, parallel, circ, remain):
    l=level
    if parpivot==2:
        for xcsc,yctc in total_adapted:
            xcsc(l)=xcsc(l-1)
            yctc(l)=yctc(l-1)
    else:
        if parpivot==1:
            aux=circ(l-1)[0:pivot]
            a=len(aux)
            simp=top.difference(parallel(l-1))

        if parpivot==3:
            aux=circ(l-1)[pivot:]#final?
            a=len(aux)
            simp=top.difference(parallel(l-1)+circ(l-1)[0:pivot-1])

        for p in range(a-2:0):
            globalmu(simp)#falta
            aux[p,p+1]=aux[p+1,p]

    for xcsc,yctc in total_adapted:
        for m in range(l+1:):#final?
            xcsc[m]=xcsc[l]
            yctc[m]=yctc[l]

    return 1

def increase(parallel, circ, remain, level):
    #stop=True # por qué lo inicializo si ya me lo dan a false como parámetro?
    stop=true
    for l in [n-1:0:-1]: #n not defined
        if remain.o(l) == circ.o(l-1)[0]:
            continue
        else:
            if len(parallel(l)) > len(parallel(l-1)):
                if paralell[l][-1] != circ[l-1][-1]:#list.o(l) ? si pone .o hay que coger el ordenado si no lo pone 
                    pivot=0# position of parallel(l) interseccion circ(l-1) en circ(l-1) plus one
                    #estamos definiendo pivot, eso significa que no necesitamos pivot como parámetro
                    parallel(l)=parallel(l-1)#union circ...
                    circ(l)# eliminar la posición pivot
                    remain(l)
                    parpivot = True #estamos definiendo parpivot, eso significa que no necesitamos parpivot como parámetro
                else:
                    pivot = len(circ(l-1))-1
                    parallel(l) = parallel(l-1)
                    circ(l) = circ(l-1)#\...
                    remain(l) = remain(l-1)# intersecion ...
                    parpivot= False
            else:
                if len(remain(l)) > len(remain(l-1)):
                    pivot= 1#position od remain ....
                    parallel(l)=parallel(l)
                    circ(l)= circ(l)#\ ...
                    remain(l)= remain(l-1)# union..
                    parpivot=False
            parallel(l+1+k)=parallel(l)#with ...
            circ(l+1+k)=circ(l)#with....
            remain(l+1+k)=remain(l)#with...
            level=l
            stop=False
    return [pivot, parpivot, level, stop]

def local_check(xc,yc,sc,tc,parallel,circ,remain) #no implementar hasta que la nCounter funcione
    #lo único que mira es que xcounter y scounter sean menores que ycounter, tcounter

def local_change(xc,sc,level,pivot,parpivot): #cambia el total adapted
    #t= ( (xsCounter), (ytcounter) )
    return True
    #indefinido

def vectToWect(Si, X,ai,aic):
    '''
        Si=(2,3,5,6) (ej)
    '''
    vect_i=makeVector(Si)
    aiUaic=ai.union(aic)
    #wectj=vectj∗partial(aj∪ ̄aj(0), ̄aj(0))∗partial( aj ∪ aj(0 : 1), ̄aj(1))∗...∗partial(aj ∪ ̄aj, ̄aj(−1));
    # * = producto de matrices? -> transponer los índices pares (?)
    for aii, index in enumerate(aic):
        vect_i=np.matmul(vect_i,X.get_partial(aiUaic, aii) if index%2==1 else np.transpose(X.get_partial(aiUaic, aii)))
    
    return unmakevector(vect_i)


def kth_steenrod_square( k, X, S):
    '''
        k>0 int
        X   BSimplex
        S a collection of pairs (ai,(xi,...)) xi<simplexsize de ai en X
        ai is a simplex in X
        #d? dimensión de todos los símplices ai, todos deben tener la misma dimensión
        1<xi<simplexsize(ai)
    '''
    T=defaultdict(lambda: False)
    #recorrer únicamente los símplices diferentes
    for i in range(0,len(S)):
        for j in range(i,len(S)):
            ai = set(S[i][0])
            aj = set(S[j][0])
            bottom = ai.union(aj)
            #rep=d+k+1-len(ai.union(aj)) d+1=len(ai) dimensión de todos los símplices ai, todos deben tener la misma dimensión
            rep = len(ai)+k-len(ai.union(aj))
            if rep>0:
                #Uddot it's a simplex of length rep so is this all the subsimplex of length rep in {0,..,n}?
                for Uddot in list(itertools.combinations(set(range(0,X.get_N())).difference(bottom), rep)):
                    top = aiUaj.union(Uddot)
                    aiC = ai.difference(aj)
                    ajC = aj.difference(ai)
                    Udot = Uddot.union(aiC).union(ajC)
                    index = calculateIndex(aiC_U_ajC,top,Udot)
                    if (v in aiC and index[v] == 0) or (v in ajC and index[v] == 1):
                        wect_i=vectToWect(S(i), X, ai, aic):
                        wect_j=vectToWect(S(j), X, aj, ajc):
                        for x, y in wect_i, wect_j:
                            if(smash( X, top, bottom, x, y))
                            T.add()
                        