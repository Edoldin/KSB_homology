from collections import deque
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
    def ordered_intersection(priorityList,intersection):
        resulting_list = [x for x in priorityList if x not in intersection]
        return resulting_list

    '''def vectToWect(Si, X,ai,aic):
        ''
            Si=(2,3,5,6) (ej)
        ''
        vect_i=makeVector(Si)
        aiUaic=ai.union(aic)
        #wectj=vectj∗partial(aj∪ ̄aj(0), ̄aj(0))∗partial( aj ∪ aj(0 : 1), ̄aj(1))∗...∗partial(aj ∪ ̄aj, ̄aj(−1));
        # * = producto de matrices? -> transponer los índices pares (?)
        for aii, index in enumerate(aic):
            vect_i=np.matmul(vect_i,X.get_partial(aiUaic, aii) if index%2==1 else np.transpose(X.get_partial(aiUaic, aii)))
        
        return unmakevector(vect_i)'''
                        