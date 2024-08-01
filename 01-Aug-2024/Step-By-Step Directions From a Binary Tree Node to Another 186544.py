# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.start = []
        self.end = []
        def helper(node, path):
    
            if not node or (self.start and self.end):
                return
            if node.val == startValue:
                self.start = path[:]
            if node.val == destValue:
                self.end = path[:]

            path.append("L")
            left = helper(node.left, path)
            path.pop()

            path.append("R")
            right = helper(node.right,path)
            path.pop()

            return 

        helper(root,[])
        start_pointer, end_pointer = 0, 0
        while start_pointer < len(self.start) and end_pointer < len(self.end):
            if self.start[start_pointer] != self.end[end_pointer]:
                break
            start_pointer += 1
            end_pointer += 1

        ups = len(self.start) - start_pointer
        rest =  ''.join(self.end[end_pointer:])
        
        return 'U'*ups + rest
        
            
    