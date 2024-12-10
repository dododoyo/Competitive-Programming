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
        max_width = 0

        while current_level:

            next_level = []
            next_offset = 0

            sorted_level = current_level[:]
            sorted_level.sort()

            left_most,right_most = sorted_level[0][0],sorted_level[-1][0]
            current_level_width = right_most - left_most +1
            max_width = max(max_width,current_level_width)

            for i,node in current_level:
                if node.left:
                    left_index = (2*i + 1)-current_offset
                    next_offset = min(next_offset,left_index)
                    next_level.append([left_index,node.left])
                if node.right:
                    right_index = (2*i + 2)-current_offset
                    next_offset = min(next_offset,right_index)
                    next_level.append([right_index,node.right])

            
            current_level = next_level[:]
            current_offset = next_offset

        return max_width
