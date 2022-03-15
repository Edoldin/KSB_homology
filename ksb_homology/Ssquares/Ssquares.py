from collections import defaultdict
from ksb_homology.BurnsideCube import BurnsideCube as BS
from ksb_homology.Utils import Utils
from itertools import combinations
import numpy as np

class Ssquares:
    @staticmethod
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
        if T[pair(0)] == False:
            T[pair(0)] = pair(1)
        else:
            T[pair(0)] = T[pair(0)] ^ pair(1)

    @staticmethod # to review, to test
    def smash(X, top, bottom, x, y ):
        n=len(top)-len(bottom)
        #uddot are the tags of the edges and n is the number of edges
        uddot=top.difference(bottom)
        #path from top to bottom sigma contains all simplex in the path
        sigma=X.path(bottom,top).reverse()
        #sk is a simplex in the tree
        for sk, k in enumerate(sigma):
            double_seqs=X.double_seq(top,bottom) #todas las posibles xcounters scounters
            def filterFunc():
                if nC1[0]==x and nC1[-1]==y:
                    return True
                else:
                    return False
            filter(filterFunc, double_seqs)

            nC=[]
            for nC1 in range(0,double_seqs): # Si n = 3 xCounter=(1,1,1)=xCounters[0]
                for nC2 in range(nC1+1,double_seqs):
                    nC.append((nC1,nC2)) #nC1 (xCounter, sCounter) nC2 (Ycounter, tCounter)

            Ssquares.global_smash(X, top, bottom, tuple(nC))
    
    @staticmethod # To test, reviewed
    def global_smash(X, top, bot, nC):
        uddot=sorted(set(top).difference(set(bot)))
        n=len(uddot)
        parallel=[[]]
        remain=[[]]
        circ=[uddot]
        for l in range(1,n):
            parallel.append(circ[0][0:l])
            circ.append(circ[0][l:n])
            remain.append([])

        nC_adapted=[]
        for xCsC_old,yCtC_old in nC:
            xCsC=[]
            yCtC=[]
            for l in range(0,n):
                xCsC[l]=list(xCsC_old)
                yCtC[l]=list(yCtC_old)
            nC_adapted.append([xCsC,yCtC])

        result=Ssquares.global_check(nC, nC_adapted, parallel, circ, remain)
        # increase will modify parallel, circ, remain, level, pivot, stop
        pivot, parpivot, level, stop = Ssquares.increase(parallel, circ, remain)
        while not stop:
            #global_change only modifies nC_adapted
            Ssquares.global_change(X, nC, nC_adapted, level, pivot, parpivot)
            result=(result+Ssquares.global_check(nC_adapted, parallel, circ))%2
            pivot, parpivot, level, stop=Ssquares.increase(parallel, circ, remain)
        return result
    '''
    #nc=((1,2,4,3,7),(1,3,2,9,9)),...
    #ncAdapted=nC_adapted
    #nCAdapted=(((1,2,4,3,7),(1,2,4,3,7),(1,3,2,9,9), (1,3,2,9,9)))
    #n va a ser el numero de aristas double_seq tendrá longitud 2n+1
    '''
    @staticmethod #to complete and test
    def global_check(nC_adapted, parallel, circ):
        output=0
        n=(len(nC_adapted[0])-1)/2
        for [xcsc,yctc] in nC_adapted:
            for l in range(0,n):
                k=len(parallel[l])
                m=len(circ[l])
                limit1=2*k+2
                limit2=2*k+2*m+2
                if xcsc[l][0:limit1] != yctc[l][0:limit1] or xcsc[l][limit1:limit2] >= yctc[l][limit1:limit2]:
                    break #comprobar que solo rompe el primer for y que la l tiene el valor que debe
            if l==n-1:
                output=(output+1)%2
        return output

    @staticmethod #Tested
    def increase(parallel, circ, remain):
        stop=False
        n=len(parallel)
        for l in range(n-1,0,-1):
            if len(parallel[l-1]) == len(parallel[l])-1:
                if parallel[l][-1] != circ[l-1][-1]:
                    pivot=circ[l-1].index(Utils.intersection(parallel[l],circ[l-1]).pop())+1
                    parallel[l]=list(parallel[l-1])
                    circ[l]=list(circ[l-1])
                    parallel[l].append(circ[l].pop(pivot))
                    parpivot=1
                    level=l
                    break
                else:
                    pivot = len(circ[l-1])-1
                    parallel[l] = list(parallel[l-1])
                    circ[l]=list(circ[l-1])
                    remain[l] = list(remain[l-1])
                    remain[l].insert(0,circ[l].pop(pivot))
                    parpivot=2
                    level=l
                    break
            else:
                if remain[l][0] != circ[l-1][0]:
                    pivot=circ[l-1].index(Utils.intersection(remain[l],circ[l-1]).pop())-1
                    circ[l]=list(circ[l-1])
                    remain[l] = list(remain[l-1])
                    remain[l].insert(0,circ[l].pop(pivot))
                    parpivot=3
                    level=l
                    break
                else:
                    level=l-1
        if level!=0:
            for k in range(level+1,n):
                circ[k]=list(circ[k-1])
                parallel[k]=list(parallel[k-1])
                parallel[k].append(circ[k].pop(0))
                remain[k] = list(remain[level])
            level=l
            stop=False
        else:
            return [0, 0, 0, True]
        return [pivot, parpivot, level, stop]

    @staticmethod #revied to test
    def global_mu(X,simp,i,j,nC_adapted,level,top):
        k=len(top)-len(simp)+1
        for xCsC, yCsC in nC_adapted:
            lxc=xCsC[level]
            lyc=yCsC[level]
            l_1, l_2, l_3=2*k-1, 2*k, 2*k+2
            xmuIn=[lxc[l_1], lxc[l_2], lxc[l_3]]
            ymuIn=[lyc[l_1], lyc[l_2], lyc[l_3]]
            
            levelmuIn=2*k-3 if k != 1 else 2*k-2

            lxc[l_1], lxc[l_2], lxc[l_3] = list(X.mu(simp, i, j, xCsC[levelmuIn],xCsC[2*level+1])[xmuIn])
            lyc[l_1], lyc[l_2], lyc[l_3] = list(X.mu(simp, i, j, yCsC[levelmuIn],yCsC[2*level+1])[ymuIn])

            for l in range(level+1,len(xCsC)):
                xCsC[l] = list(xCsC[level])
                yCsC[l] = list(yCsC[level])
            

    @staticmethod #revied to test
    def global_change(top, pivot, parpivot, level, nC_adapted, parallel, circ):
        if parpivot==2:
            for xcsc,yctc in nC_adapted:
                xcsc[level]=list(xcsc[level-1])
                yctc[level]=list(yctc[level-1])
        else:
            if parpivot==1:
                aux=circ[level-1][0:pivot-1]
                a=len(aux)
                simp=Utils.ordered_difference(top,parallel[level-1])
            if parpivot==3:
                aux=circ[level-1][pivot+1:]
                a=len(aux)
                simp=Utils.ordered_difference(top,Utils.ordered_union(parallel[level-1],circ[level-1])[0:pivot-1]) # cuidado con los paréntesis, bien(?)
            for p in range(a-2,0,-1):
                Ssquares.globalmu(Utils.ordered_difference(simp,aux[0:p-1]),aux[p],aux[p+1],nC_adapted,level)#falta
                aux[p,p+1]=aux[p+1,p]

        for xcsc,yctc in nC_adapted:
            for m in range(level+1,len(xcsc)): #está bien (?)
                xcsc[m]=xcsc[level]
                yctc[m]=yctc[level]
        return 1    

    @staticmethod #to review
    def global_check(nCAdapted, parallel, circ, remain):
        output=0
        n=len(parallel)-1
        for xcsc,yctc in nCAdapted:
            for l in range(n):
                k = len(parallel[l])
                m = len(circ[l])
                if xcsc[l][0:2*k+1] != yctc[l][0:2*k+1] or xcsc[l][0:2*k+1] != yctc[l][0:2*k+1]:
                    break
            if l is n-1:
                output += 1
        return output
    #def local_check(xc,yc,sc,tc,parallel,circ,remain): #no implementar hasta que la double_seq funcione
    #lo único que mira es que xcounter y scounter sean menores que ycounter, tcounter

    #def local_change(xc,sc,level,pivot,parpivot): #cambia el nC adapted
    #t= ( (xsCounter), (ytcounter) )
    #    return True
    #indefinido

    @staticmethod
    def vectToWect(Si, X,ai,aic):
        '''
            Si=(2,3,5,6) (ej)
        '''
        vect_i=Ssquares.makeVector(Si)
        aiUaic=ai.union(aic)
        #wectj=vectj∗partial(aj∪ ̄aj(0), ̄aj(0))∗partial( aj ∪ aj(0 : 1), ̄aj(1))∗...∗partial(aj ∪ ̄aj, ̄aj(−1));
        # * = producto de matrices? -> transponer los índices pares (?)
        for aii, index in enumerate(aic):
            vect_i=np.matmul(vect_i,X.get_partial(aiUaic, aii) if index%2==1 else np.transpose(X.get_partial(aiUaic, aii)))
        
        return Ssquares.unmakevector(vect_i)

    @staticmethod
    def kth_steenrod_square( k, X, S):
        '''
            k>0 int
            X   BurnsideCube
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
                    #Uddot it's a simplex of length rep so is this all the suBurnsideCube of length rep in {0,..,n}?
                    for Uddot in list(combinations(set(range(0,X.get_N())).difference(bottom), rep)):
                        top = bottom.union(Uddot)
                        aiC = ai.difference(aj)
                        ajC = aj.difference(ai)
                        aiC_U_ajC=aiC.union(ajC)
                        Udot = Uddot.union(aiC_U_ajC)
                        index = Utils.calculateIndex(aiC_U_ajC,top,Udot)
                        '''
                        if (v in aiC and index[v] == 0) or (v in ajC and index[v] == 1):
                            wect_i=Ssquares.vectToWect(S(i), X, ai, aiC)
                            wect_j=Ssquares.vectToWect(S(j), X, aj, ajC)
                            for x, y in wect_i, wect_j:
                                if(Ssquares.smash( X, top, bottom, x, y)):
                                    Ssquares.add(T,Ssquares.globalsmash(top,bottom,x,y))
                        '''
