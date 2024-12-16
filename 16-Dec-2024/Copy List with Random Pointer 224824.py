# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

class Solution:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, node: "Optional[Node]") -> "Optional[Node]":
        if not node:
            return node 

        # if the curr node is already copied 
        # return the copied node 
        if node in self.visited:
            return self.visited[node]

        node_copy = Node(node.val)

        self.visited[node] = node_copy
        node_copy.next = self.copyRandomList(node.next)
        node_copy.random = self.copyRandomList(node.random)
        
        return self.visited[node]

