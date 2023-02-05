class MyCircularDeque:
    
  
    def __init__(self, k: int):
        self.max_length = k
        self.size = 0
        self.answer = [None]*k
        self.last = 0
        self.first = 0
        
    def insertFront(self, value: int) -> bool:
        
        if(self.isEmpty()):
            self.answer[self.first] = value
            self.size += 1
            return True
        
        elif(not self.isFull()):
            self.first = (self.first -1 ) % self.max_length
            self.answer[self.first] = value
            self.size += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        
        if(self.isEmpty()):
            self.answer[self.last] = value
            self.size += 1
            return True
        
        elif(not self.isFull()):
            self.last = (self.last + 1)%self.max_length
            self.answer[self.last] = value
            self.size += 1
            return True
        else:
            return False
        
    def deleteFront(self) -> bool:
        if(not self.isEmpty()):
            self.answer[self.first] = None
            if(self.size != 1):
                self.first = (self.first +1)%self.max_length
            self.size -= 1
            return True
        else:
            return False
        
    def deleteLast(self) -> bool:
        if(not self.isEmpty()):
            self.answer[self.last] = None
            if (self.size != 1):
                self.last = (self.last -1)% self.max_length
            self.size -= 1
            return True
        else:
            return False
        

    def getFront(self) -> int:
        if(not self.isEmpty()):
            return self.answer[self.first]
        else:
            return -1
        

    def getRear(self) -> int:
        if(not self.isEmpty()):
            return self.answer[self.last]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.max_length
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()