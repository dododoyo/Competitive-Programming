# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

class Solution:
    def __init__(self):
        self.visited = {}

    def getClone(self,node):
        # node 
        if node:
            # node is copied before 
            if node in self.visited:
                # return previous copied node 
                return self.visited[node]
            # node is seen for the first time
            else:
                # clone node 
                clone = Node(node.val)
                # and return clone 
                self.visited[node] = clone
                return self.visited[node]
        # null pointer 
        else:
            return None

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # use iteration 
        if not head:
            return head 

        # clone the head 
        old_head = head
        new_head = Node(old_head.val)
        self.visited[old_head] = new_head

        # clone the whole linkedlist with iteration
        while old_head:
            new_head.next = self.getClone(old_head.next)
            new_head.random = self.getClone(old_head.random)

            old_head = old_head.next
            new_head = new_head.next
        
        return self.visited[head]
