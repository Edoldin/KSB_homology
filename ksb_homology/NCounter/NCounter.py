class NCounter(tuple):
    def __new__(self, p_tuple):
        return tuple.__new__(NCounter, p_tuple)

    def getXkey(self):
        vector=[self[0]]
        for i in range(1,len(self)):
            if i%2!=0:
                vector.append(self[i])
        return vector

    def getSkey(self):
        vector=[]
        for i in range(2,len(self)):
            if i%2==0:
                vector.append(self[i])
        return vector

    @staticmethod
    def mergeVertexAxis(vertexValues,edges):
        vector=[vertexValues[0]]
        for i,e in enumerate(edges):
            vector.extend([vertexValues[i+1],e])
        return NCounter(vector)

    @staticmethod
    def lexicographicNextValue(value,bound):
        k=len(bound)-1
        value[k]+=1
        while bound[k]<value[k] and k>0:
            value[k]=0
            k-=1
            value[k]+=1
        return value

    @staticmethod
    def arrayBiggerThan(bigger,smaller):
        if len(bigger) != len(smaller):
            return False
        k=0
        while bigger[k]==smaller[k] and k<len(bigger)-1:
            k+=1
        return bigger[k]>smaller[k]

    @staticmethod
    def listOrder(list1, list2):
        k=0
        while k<len(list1):
            if list1[k]!=list2[k]:
                return list1[k]>list2[k]
            k+=1
        return True
    