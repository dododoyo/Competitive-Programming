# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node):
        if not node:
            return 0,True

        left_h = self.dfs(node.left)
        right_h = self.dfs(node.right)

        if left_h[0] == -1 or right_h[0] == -1:
            return -1,False

        if abs(left_h[0]-right_h[0]) > 1:
            return -1,False
        else:
            return 1 + max(left_h[0],right_h[0]),True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[1]