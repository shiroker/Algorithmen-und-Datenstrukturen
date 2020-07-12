from ADTList import ADTList
class ADTStack:
    elements = ADTList()
    counter = 0

    def __init__(self):
        self.elements = ADTList()
        self.counter = 0
    def push(self, elem):
        self.elements.addElem(self.counter, elem)
        self.counter += 1

    def pop(self):
        if self.counter == 0: return
        self.counter -= 1

    def top(self):
        if self.counter == 0: return None
        return self.elements.getElem(self.counter-1)

    def isEmpty(self):
        return self.counter == 0

    def laenge(self):
        return self.counter

    def equals(self,other):
        if isinstance(other, ADTStack):
            if self.laenge() != other.laenge(): return False
            if self.isEmpty() and other.isEmpty: return True
            dummy = other
            for i in range(0,self.laenge()):
                if self.top() != dummy.top(): return False
                dummy.pop()
            return True

    def reverse(self):
        dummy = ADTStack()
        for i in range(0, self.counter-1):
            dummy.push(self.top())
            self.pop()
        return dummy




