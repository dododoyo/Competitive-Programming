import random
class RandomizedSet:
    def __init__(self):
        self.rand_set = list() 
        self.index_map = dict()
    def insert(self, val: int) -> bool:
        in_set = val in self.index_map
        if not in_set:
            self.index_map[val] = len(self.rand_set)
            self.rand_set.append(val)
        return not in_set
    def remove(self, val: int) -> bool:
        if val in self.index_map:
            val_index,last_index  = self.index_map[val], len(self.rand_set)-1
            self.index_map[self.rand_set[last_index]] = val_index
            self.rand_set[val_index],self.rand_set[last_index] = self.rand_set[last_index],self.rand_set[val_index] 
            self.rand_set.pop()
            self.index_map.pop(val)
            return True
        return False
    def getRandom(self) -> int:
        return self.rand_set[random.randint(0, len(self.rand_set)-1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()