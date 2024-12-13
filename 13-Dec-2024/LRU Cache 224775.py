# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class LRUNode:
    def __init__(self,_key,_val,_next=None,_prev=None):
        self.key = _key
        self.val = _val
        self.next = _next
        self.prev = _prev

class LRUCache:

    def __init__(self, capacity: int):
        # init cache dictionary  
        # key:int , val:LRUNode
        self.cache = {}
        self.top = LRUNode(-1,-1)
        self.bottom = LRUNode(-1,-1)
        self.capacity = capacity

        # form the linkedlist
        self.bottom.next = self.top
        self.top.prev = self.bottom

    def add(self,node):
        node.prev = self.top.prev
        node.next = self.top

        self.top.prev = node
        node.prev.next = node

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = LRUNode(key,value)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.bottom.next
            self.remove(lru)
            del self.cache[lru.key]
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)