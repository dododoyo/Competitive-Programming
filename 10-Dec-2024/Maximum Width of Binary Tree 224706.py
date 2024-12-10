# Problem: Maximum Width of Binary Tree - https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        current_level = [[0,root]]
        current_offset = 0
        max_width = 1

        while current_level:

            next_level = []
            next_offset = 0

            left_most = float('inf')
            right_most = -float('inf')

            for i,node in current_level:
                if node.left:
                    left_index = (2*i + 1)-current_offset
                    next_offset = min(next_offset,left_index)
                    next_level.append([left_index,node.left])

                    left_most = min(left_most,left_index)
                    right_most = max(right_most,left_index)
                if node.right:
                    right_index = (2*i + 2)-current_offset
                    next_offset = min(next_offset,right_index)
                    next_level.append([right_index,node.right])

                    left_most = min(left_most,right_index)
                    right_most = max(right_most,right_index)

            current_level_width = right_most - left_most +1
            max_width = max(max_width,current_level_width)

            current_level = next_level[:]
            current_offset = next_offset

        return max_width
