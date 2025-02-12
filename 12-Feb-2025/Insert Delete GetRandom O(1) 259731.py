# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

from random import randint
class RandomizedSet:
    # we could have used only set to solve this problem 
    # if the only methods required was insert and remove
    # but getting a random element will be difficult 
    # if we are only using sets so . . . 

    # for that we will use lists

    def __init__(self):
        self.index_map = {}
        self.list_elements = []
        

    def insert(self, val: int) -> bool:
        if not (val in self.index_map):
            self.index_map[val] = len(self.list_elements)
            self.list_elements.append(val)
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.index_map:
            # swap with the last element and pop 
            curr = self.index_map[val]

            # update index of element before swapping
            self.index_map[self.list_elements[-1]] = curr
            self.list_elements[-1],self.list_elements[curr] = self.list_elements[curr],self.list_elements[-1]

            # delete from the map
            del self.index_map[self.list_elements[-1]]

            # delete from the list
            self.list_elements.pop()

            return True

        return False


    def getRandom(self) -> int:
        idx = randint(0,len(self.list_elements)-1)
        return self.list_elements[idx]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()