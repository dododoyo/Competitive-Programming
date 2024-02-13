class AdvancedNode:
    def __init__(self,key_,val_,prev_=None,next_=None):
        self.val = val_
        self.key = key_
        self.prev = prev_
        self.next = next_

class LRUCache:
    """
    LRU Cache has the property of removing the least recently
    used data from the cache so whenever the cache is full we
    must remove it the Least recently used data.
    
    The idea of using a node means making it the most recent"""
    def removeNode(self,node):
            prev_node = node.prev
            next_node = node.next

            prev_node.next = next_node
            next_node.prev = prev_node 
    def insertAtRight(self,node):
        before_right = self.right_most.prev

        node.next = self.right_most
        node.prev = before_right

        self.right_most.prev = node
        before_right.next = node

    def __init__(self, capacity: int):
        # dictionary depiciton of the cache
        self.cache = {}

        # maximum capacity the cache can hold
        self.capacity = capacity

        """
        Creating two dummy nodes to encapsulate 
        our whole linkedlist and connecting them
        to each other """
        self.left_most = AdvancedNode(0,0)
        self.right_most = AdvancedNode(0,0,prev_=self.left_most)
        self.left_most.next = self.right_most        

    def get(self, key: int) -> int:
        if key in self.cache:
            # if the key is in cache 
            # make it the most recently used 
            inserted_node = self.cache[key]
            self.removeNode(inserted_node)
            self.insertAtRight(inserted_node)
            return inserted_node.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])
            
        inserted_node = AdvancedNode(key,value)

        # update the cache value
        self.cache[key] = inserted_node
        # make the new node the most recently used
        self.insertAtRight(inserted_node)

        if self.capacity < len(self.cache):
            # remove the least recently used cache
            # which is the one next to the left most
            del self.cache[self.left_most.next.key]
            self.removeNode(self.left_most.next)
    
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)