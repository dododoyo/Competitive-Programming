# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        solution = []
        def dfs(node):
            if not node:
                return 

            solution.append(str(node.val))

            if not (node.left or  node.right):
                return 

            # the left child is never ignored for meeting the 
            # one to one mapping of string and tree
            
            solution.append("(")
            dfs(node.left)
            solution.append(")")

            if node.right:
                solution.append("(")
                dfs(node.right)
                solution.append(")")
            return 

        dfs(root)
        return "".join(solution)