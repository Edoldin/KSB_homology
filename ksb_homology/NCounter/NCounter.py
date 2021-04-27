import bisect
import itertools

class NCounter(Tuple):
    def getXkey(self):
        vector=[self[0]]
        for i in range(1,len(self)):
            if i%2!=0:
                vector.append(self(i))
        return vector

    def getSkey(self):
        vector=[]
        for i in range(2,len(self)):
            if i%2==0:
                vector.append(self(i))
        return vector

    @staticmethod
    def mergeVertexAxis(vertexValues,edges):
        vector=[]
        for i,e in enumerate(edges):
            vector.extend([vertexValues[i],e])
        vector.append(vertexValues[-1])
        return Ncounter(vector)

    @staticmethod
    def lexicographicNextValue(value,bound):
        k=len(bound)-1
        value[k]+=1
        while bound[k]<value[k] and k>0:
            value[k]=1
            k-=1
            value[k]+=1
        return value

    @staticmethod
    def listOrder(list1, list2):
        k=0
        while k<len(list1):
            if list1[k]!=list2[k]:
                return list1[k]>list2[k]
            k+=1
        return True

    @staticmethod
    def getVertexDifPosition(vertexValues):
        for v,k in enumerate(vertexValues):
            if(v!=1):
                return k
        return 0
    