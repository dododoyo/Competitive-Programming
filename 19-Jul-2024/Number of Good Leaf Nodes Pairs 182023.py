# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        self.solution = 0
        def helper(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            
            left = helper(node.left)
            right = helper(node.right)
            for l_h in left:
                for r_h in right:
                    if l_h + r_h <= distance:
                        self.solution += 1
            
            new_h = []
            for h in left + right:
                if h < distance:
                    new_h.append(h + 1)
            
            return new_h

        helper(root)
        return self.solution
            
        