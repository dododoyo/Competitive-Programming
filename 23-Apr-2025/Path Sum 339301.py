# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        current_level = []
        last_level = []

        if root:current_level.append([root,targetSum])

        while current_level:
            next_level = []

            for node,currTarget in current_level:
                # check if leaf 
                if (not node.left) and (not node.right):
                    if currTarget == node.val:
                        return True

                if node.left:
                    next_level.append([node.left,currTarget-node.val])
                if node.right:
                    next_level.append([node.right,currTarget-node.val])

            current_level = next_level[:]

        return False