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
            return left.val == right.val and self.dfs(left.right,right.left) and self.dfs(left.left,right.right)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # do dfs on both childs 
        return self.dfs(root.right,root.left)
        