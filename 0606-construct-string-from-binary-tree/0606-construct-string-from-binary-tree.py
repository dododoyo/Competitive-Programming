# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        
        if left or right:
            return f"{t.val}({left}){'' if not right else f'({right})'}"
        else:
            return str(t.val)