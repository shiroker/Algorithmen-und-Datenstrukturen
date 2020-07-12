class ADTList:
   
    elemList = {}
    counter = 0
    
    indexList = []
    
 
    def __init__(self):
        self.elemList = {}
        self.counter = 0
        self.indexList = []
 
    def getElem(self, index):
        
        if(index >= 0): return self.elemList.get(index)
        return "der Index soll keine negative Zahl sein"
        
    def getAllElems(self):
        dummy = []
        for x in self.indexList:
            dummy.append(self.elemList.get(x))
        return dummy

    def getMeHash(self):
        dummy = {}
        for x in self.indexList:
            dummy.update({x: self.elemList.get(x)})
        return dummy
    
        # hier ein String- oder Chracter-Eintrag ist gleich wie ein Character-Eintrag
    def addElem(self, index, elem):
        if(index < 0): return "der eingegebene index soll >= 0"
        
        if(self.indexList.__contains__(index)):
            self.elemList.update({index:elem})
            
        else:
            self.indexList.append(index)
            self.elemList.update({index:elem})
            self.counter += 1
            self.indexList.sort()
        return

    def retrieve(self, index):
        if(self.elemList.keys().__contains__(index)): 
            dummy = self.getElem(index)
            self.deleteElem(index)
            
            return dummy
        else: 
            return "der angegebene Index war bisher nicht besetzt"
        return
        

    
    def deleteElem(self, index):
       
        if(self.elemList.keys().__contains__(index)): 
            self.elemList.__delitem__(index)
            self.counter -=1
        else: 
            return "der angegebene Index war bisher nicht besetzt"
        return
            
        
    def laenge(self):
        if self.counter > 0:
            return self.indexList[-1]
        return self.counter

    def isEmpty(self): 
        return self.counter == 0

    def equals(self, other ):
        if isinstance(other, ADTList):
            if(self.indexList[-1] != other.laenge()): return False
            else:
                for x in self.indexList:
                    if self.getElem(x) != other.getElem(x): return False
        return True

    
    







