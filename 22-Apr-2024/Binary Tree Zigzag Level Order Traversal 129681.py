# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        current_level,solution,right_to_left = [root],[[root.val]],False

        while current_level:
            next_level,next_level_value = [],[]

            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                    next_level_value.append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    next_level_value.append(node.right.val)

            if next_level_value:
                if right_to_left:
                    solution.append(next_level_value)
                else:
                    solution.append(next_level_value[::-1])

            current_level  = next_level
            right_to_left = not right_to_left

        return solution 