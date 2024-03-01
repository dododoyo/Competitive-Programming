# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        solution = []
        def helper(current):
            if not current:
                return None
            helper(current.left)
            solution.append(current.val)
            helper(current.right)
            return None
        helper(root)
        return solution[k-1]