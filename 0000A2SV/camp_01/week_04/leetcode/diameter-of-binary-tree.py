# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # using array as primitive
        diameter = [0]
        def helper(curr):
            if not curr:
                return 0
            right_depth = helper(curr.right)
            left_depth = helper(curr.left)
            diameter[0] = max(diameter[0],right_depth+left_depth)
            return max(right_depth,left_depth) + 1
        helper(root)
        return diameter[0]