# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,right,left):
            if not (right or left):
                return True
            if not right or not left:
                return False
                f
            # values must be same 
            values_valid = left.val == right.val

            # left of right must be equal to right of left
            cross = self.dfs(left.right,right.left)

            # left of left must be equal to right of right
            same = self.dfs(left.left,right.right)

            return values_valid and cross and same
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # do dfs on both childs 
        return self.dfs(root.right,root.left)
        