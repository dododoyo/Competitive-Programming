# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node,solution):
        if node:
            solution.append(node.val)
            self.dfs(node.left,solution)
            self.dfs(node.right,solution)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        solution = []
        self.dfs(root,solution)
        return solution

        