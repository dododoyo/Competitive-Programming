#define class for nodes
class Node:
    def __init__(self,key,val):
        self.key,self.val = key,val;
        self.prev = self.next = None;
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity;
        self.cache = { }
        self.left,self.right = Node(0,0), Node(0,0);
        
        #connect the nodes
        self.left.next,self.right.prev = self.right,self.left;
    
    def removeNode(self,node):
        node.prev.next = node.next;
        node.next.prev = node.prev
        
    def insertAtRight(self,node):
        # thePrev = self.right.prev;
        
        self.right.prev.next = node
        node.prev = self.right.prev
        
        self.right.prev = node;
        node.next = self.right
        
        # thePrev.next = node
        # node.prev = thePrev
        
        
        self.right.prev
         
    def get(self, key: int) -> int:
        if key in self.cache:
            #removing key value pair from linkedlist 
            #not from the hashmap
            self.removeNode(self.cache[key]);
            
            '''moving it to the right most because it is the most
            recenlty used'''
            
            self.insertAtRight(self.cache[key]);
            return self.cache[key].val;
        else:return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key]);
        self.cache[key] = Node(key,value);
        self.insertAtRight(self.cache[key])
        
        if len(self.cache) > self.cap:
            del self.cache[self.left.next.key];
            self.removeNode(self.left.next);
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)