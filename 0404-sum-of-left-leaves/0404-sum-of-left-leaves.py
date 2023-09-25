# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sol = 0;
        def helper(root):
            nonlocal sol
            if root:
                if root.left and ((not root.left.left) and (not root.left.right)):
                    sol += root.left.val;
                    
                helper(root.left);
                helper(root.right);
        helper(root);
        return sol
                