#we need nodes to implement a linkedlist
class ListNode:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
class MyLinkedList:

    def __init__(self):
        #creating the dummy nodes
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        #return the value of the node at specific index
        current_node = self.left.next
        i = 0
        while current_node != None and i < index:
            current_node = current_node.next;i+=1
        if current_node != None and current_node != self.right and i == index:
            return current_node.val
        return -1
             

    def addAtHead(self, val: int) -> None:
        #inserts a new node at the head with the given value
        curr_node = ListNode(val)
        next_node = self.left.next
        prev_node = self.left
        
        curr_node.next = next_node
        curr_node.prev = prev_node
        
        prev_node.next = curr_node
        next_node.prev = curr_node
    def addAtTail(self, val: int) -> None:
        #inserts a new node at the tail with the given value
        curr_node = ListNode(val)
        next_node = self.right
        prev_node = self.right.prev
        
        curr_node.next = next_node
        curr_node.prev = prev_node
        
        prev_node.next = curr_node
        next_node.prev = curr_node

    def addAtIndex(self, index: int, val: int) -> None:
        #adds a node at specific index
        current_node,i = self.left.next,0
        while current_node != None and i < index:
            current_node = current_node.next;i+=1
        if current_node != None and i == index:
            node_added = ListNode(val)
            next_node = current_node
            prev_node = current_node.prev
            
            node_added.next = next_node
            node_added.prev = prev_node
            
            prev_node.next = node_added
            next_node.prev = node_added 
            

    def deleteAtIndex(self, index: int) -> None:
        #remove from specific index
        current_node,i = self.left.next,0
        while current_node != None and i < index:
            current_node = current_node.next;i+=1
        if current_node != None and current_node != self.right and i == index:
            next_node = current_node.next
            prev_node = current_node.prev
            
            
            prev_node.next = next_node
            next_node.prev = prev_node
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)