class Bitset:
    def __init__(self, size: int):
        self.bits = [0] * size
        self.ones = 0
        self.flipped = False
    
    def fix(self, idx: int) -> None:
        if self.flipped:
            if self.bits[idx] == 1: 
                self.ones += 1
            self.bits[idx] = 0
        else:
            if self.bits[idx] == 0: 
                self.ones += 1
            self.bits[idx] = 1
    
    def unfix(self, idx: int) -> None:
        if self.flipped:
            if self.bits[idx] == 0: 
                self.ones -= 1
            self.bits[idx] = 1
        else: 
            if self.bits[idx] == 1: 
                self.ones -= 1
            self.bits[idx] = 0
    
    def flip(self) -> None:
        self.flipped = not self.flipped
        self.ones = len(self.bits) - self.ones
    
    def all(self) -> bool: 
        return self.ones == len(self.bits)

    def one(self) -> bool: 
        return self.ones > 0 

    def count(self) -> int: 
        return self.ones
        
    def toString(self) -> str: 
        return ''.join([str(0 if i else 1) for i in self.bits]) if self.flipped else ''.join([str(i) for i in self.bits])
# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()