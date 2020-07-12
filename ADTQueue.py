from ADTStack import ADTStack


class ADTQueue:

    inStack = ADTStack()
    outStack = ADTStack()
    counter = 0


    def __init__(self):
        self.inStack = ADTStack()
        self.outStack = ADTStack()
        self.counter = 0

    def enqueue(self, elem):
        self.inStack.push(elem)
        self.counter += 1


    def dequeue(self):
        if self.counter == 0: return "Queue ist noch leer"
        if self.outStack.isEmpty():
            for i in range(0,self.inStack.laenge()):
                self.outStack.push(self.inStack.top())
                self.inStack.pop()
        self.outStack.pop()
        self.counter -= 1

    def front(self):
        if self.counter == 0: return "Queue ist noch leer"
        if self.outStack.isEmpty():
            for i in range(0,self.inStack.laenge()):
                self.outStack.push(self.inStack.top())
                self.inStack.pop()
        return self.outStack.top()

    def isEmpty(self):
        return self.counter == 0

    def  laenge(self):
        return self.counter

    def equals(self, other):
        if isinstance(other, ADTQueue):
            
            if self.laenge() != other.laenge(): return False
            dummySelf = []
            dummyOther =[]
            for x in range(0,other.laenge()):
                if self.front() != other.front(): return False
                dummySelf.append(self.front())
                dummyOther.append(other.front())
                self.dequeue()
                other.dequeue()
            for y in range(0,len(dummySelf)):
                self.enqueue(dummySelf.__getitem__(y))
                other.enqueue(dummyOther.__getitem__(y))
                pass
            return True
            
        


    def reverse(self):
        dummyIn = self.inStack
        dummyOut = self.outStack
        self.inStack = dummyOut
        self.outStack = dummyIn

    